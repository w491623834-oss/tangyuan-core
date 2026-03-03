"""
Connection Pool Module for tangyuan-core v1.1.0.
Reuses active connections to minimize latency and overhead.
"""
import asyncio
from collections import deque
from typing import Optional, Dict, Any
try:
    from .socket_client import AsyncSecureSocket
    from .adaptive_net import probe_network, NetworkMode, get_config
except ImportError:
    from socket_client import AsyncSecureSocket
    from adaptive_net import probe_network, NetworkMode, get_config

class ConnectionPool:
    def __init__(self, host: str, port: int, max_size: int = 5):
        self.host = host
        self.port = port
        self.max_size = max_size
        self._pool: deque = deque()
        self._lock = asyncio.Lock()
        self._closed = False
        
    async def acquire(self) -> AsyncSecureSocket:
        """Get a connection from the pool or create a new one."""
        async with self._lock:
            if self._pool:
                conn = self._pool.popleft()
                # Check if connection is still alive (simplified)
                if not conn._writer.is_closing():
                    return conn
            # Create new connection if pool is empty or connection is dead
            return await self._create_connection()
    
    async def release(self, conn: AsyncSecureSocket):
        """Return a connection to the pool."""
        if self._closed or len(self._pool) >= self.max_size or conn._writer.is_closing():
            await conn.close()
        else:
            self._pool.append(conn)
            
    async def _create_connection(self) -> AsyncSecureSocket:
        """Internal method to create a new connection."""
        # Auto-detect network mode for optimal config
        # (In real usage, we might cache this result)
        mode = await probe_network(self.host, self.port)
        config = get_config(mode)
        
        conn = AsyncSecureSocket(self.host, self.port, timeout=config.timeout)
        await conn.connect()
        return conn

    async def close(self):
        """Close all connections in the pool."""
        self._closed = True
        while self._pool:
            conn = self._pool.popleft()
            await conn.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

# Usage Example
async def main():
    pool = ConnectionPool("www.google.com", 443)
    
    # Acquire connection 1
    conn1 = await pool.acquire()
    print(f"Conn 1 acquired. Pool size: {len(pool._pool)}")
    
    # Release it
    await pool.release(conn1)
    print(f"Conn 1 released. Pool size: {len(pool._pool)}")
    
    # Acquire again (should reuse)
    conn2 = await pool.acquire()
    print(f"Conn 2 acquired (reused?). Pool size: {len(pool._pool)}")
    
    await pool.close()
    print("Pool closed.")

if __name__ == "__main__":
    asyncio.run(main())
