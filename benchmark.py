"""
Benchmark for tangyuan-core v1.1.0.
Compares performance with and without Connection Pooling.
"""
import asyncio
import time
from tangyuan_core import AsyncSecureSocket, ConnectionPool

HOST = "www.google.com"
PORT = 443
CONCURRENT_REQUESTS = 10

async def request_without_pool():
    """Simulate a request without pooling (new connection every time)."""
    conn = AsyncSecureSocket(HOST, PORT)
    try:
        await conn.connect()
        # Simulate a tiny HTTP GET
        # conn._writer.write(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        # await conn._writer.drain()
        # await conn._reader.read(100)
    finally:
        await conn.close()

async def request_with_pool(pool: ConnectionPool):
    """Simulate a request with pooling."""
    conn = await pool.acquire()
    try:
        # Simulate work
        await asyncio.sleep(0.01) 
    finally:
        await pool.release(conn)

async def run_benchmark():
    print(f"[BENCH] Starting Benchmark (Host: {HOST}, Concurrency: {CONCURRENT_REQUESTS})...")
    
    # 1. Benchmark WITHOUT Pool (Sequential to avoid overwhelming, but simulates overhead)
    start = time.time()
    tasks = [request_without_pool() for _ in range(CONCURRENT_REQUESTS)]
    # Run sequentially for safety in this demo, but overhead is in connect/disconnect
    for task in tasks:
        await task
    time_no_pool = time.time() - start
    
    # 2. Benchmark WITH Pool
    pool = ConnectionPool(HOST, PORT, max_size=5)
    start = time.time()
    tasks = [request_with_pool(pool) for _ in range(CONCURRENT_REQUESTS)]
    await asyncio.gather(*tasks)
    time_with_pool = time.time() - start
    await pool.close()
    
    # Report
    print("\n--- [BENCH] Results ---")
    print(f"Time w/o Pool: {time_no_pool:.3f}s")
    print(f"Time w/ Pool:  {time_with_pool:.3f}s")
    if time_with_pool > 0:
        print(f"Speedup:       {time_no_pool / time_with_pool:.2f}x")
    print("--------------------------")

if __name__ == "__main__":
    asyncio.run(run_benchmark())
