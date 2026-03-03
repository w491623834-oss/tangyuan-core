"""
Async Native Socket Client - Zero dependency, high performance.
Uses Python standard library: asyncio, ssl, json.
Inspired by: websockets, aiohttp, MicroPython memory efficiency.
"""

import asyncio
import ssl
import json
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class AsyncSecureSocket:
    """
    Ultra-lightweight async socket client.
    Features:
    - Non-blocking I/O (asyncio)
    - Native SSL/TLS support
    - Auto-reconnect with exponential backoff
    - Memory-efficient streaming
    - Zero external dependencies
    """
    
    def __init__(self, host: str, port: int, use_ssl: bool = True, timeout: int = 30):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.timeout = timeout
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._reconnect_delay = 1.0
        self._max_reconnect_delay = 60.0
        
    async def connect(self):
        """Establish async connection with SSL support."""
        try:
            ssl_context = ssl.create_default_context() if self.use_ssl else None
            self._reader, self._writer = await asyncio.open_connection(
                self.host, 
                self.port,
                ssl=ssl_context,
                server_hostname=self.host if self.use_ssl else None
            )
            self._reconnect_delay = 1.0  # Reset delay on success
            logger.info(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            logger.warning(f"Connection failed: {e}")
            raise
    
    async def send(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send JSON data and receive response asynchronously.
        
        Args:
            data: Dictionary to send as JSON
            
        Returns:
            Response dictionary
        """
        if not self._writer or self._writer.is_closing():
            await self.connect()
        
        try:
            # Send JSON
            payload = json.dumps(data).encode('utf-8')
            self._writer.write(payload)
            self._writer.write(b'\n')  # Line-based protocol
            await self._writer.drain()
            
            # Receive response (line-based)
            response_line = await self._reader.readline()
            if not response_line:
                raise ConnectionError("Connection closed by server")
            
            return json.loads(response_line.decode('utf-8'))
            
        except Exception as e:
            logger.error(f"Send/receive error: {e}")
            self._writer.close()
            await self._writer.wait_closed()
            raise
    
    async def send_with_retry(self, data: Dict[str, Any], max_retries: int = 3) -> Dict[str, Any]:
        """
        Send with exponential backoff retry logic.
        Inspired by CCXT's retry mechanism.
        """
        last_error = None
        
        for attempt in range(max_retries):
            try:
                return await self.send(data)
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    logger.warning(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
                    await asyncio.sleep(self._reconnect_delay)
                    # Exponential backoff
                    self._reconnect_delay = min(
                        self._reconnect_delay * 2, 
                        self._max_reconnect_delay
                    )
        
        raise last_error
    
    async def close(self):
        """Close connection gracefully."""
        if self._writer:
            self._writer.close()
            await self._writer.wait_closed()
            self._writer = None
            self._reader = None
    
    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

# Sync wrapper for backward compatibility
class SecureSocket:
    """Synchronous wrapper for AsyncSecureSocket (legacy compatibility)."""
    
    def __init__(self, host: str, port: int, use_ssl: bool = True, timeout: int = 30):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.timeout = timeout
        
    def send(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sync wrapper using asyncio.run()."""
        async def _send():
            async with AsyncSecureSocket(self.host, self.port, self.use_ssl, self.timeout) as client:
                return await client.send(data)
        
        return asyncio.run(_send())
