"""
Adaptive Network Module for tangyuan-core v1.1.0.
Auto-adjusts connection parameters based on real-time network conditions.
"""
import asyncio
import socket
import time
from enum import Enum

class NetworkMode(Enum):
    FAST = "FAST"       # <50ms latency
    NORMAL = "NORMAL"   # 50-200ms
    SLOW = "SLOW"       # >200ms

class AdaptiveConfig:
    def __init__(self, mode: NetworkMode):
        self.mode = mode
        if mode == NetworkMode.FAST:
            self.timeout = 5.0
            self.retries = 1
            self.tcp_nodelay = True
            self.buffer_size = 4096
        elif mode == NetworkMode.NORMAL:
            self.timeout = 15.0
            self.retries = 3
            self.tcp_nodelay = False
            self.buffer_size = 8192
        else: # SLOW
            self.timeout = 30.0
            self.retries = 5
            self.tcp_nodelay = False
            self.buffer_size = 16384

async def probe_network(host: str, port: int) -> NetworkMode:
    """
    Probe network latency to host and return optimal mode.
    """
    start = time.time()
    try:
        # Async TCP Connect Test
        reader, writer = await asyncio.open_connection(host, port)
        latency = (time.time() - start) * 1000  # ms
        writer.close()
        await writer.wait_closed()
        
        if latency < 50:
            print(f"[NET] Fast network detected ({latency:.1f}ms). Mode: FAST")
            return NetworkMode.FAST
        elif latency < 200:
            print(f"[NET] Normal network detected ({latency:.1f}ms). Mode: NORMAL")
            return NetworkMode.NORMAL
        else:
            print(f"[NET] Slow network detected ({latency:.1f}ms). Mode: SLOW")
            return NetworkMode.SLOW
    except Exception as e:
        print(f"[NET] Probe failed ({e}). Defaulting to SLOW mode.")
        return NetworkMode.SLOW

def get_config(mode: NetworkMode) -> AdaptiveConfig:
    return AdaptiveConfig(mode)

# Example usage within the core
async def main():
    # Test against a known host
    mode = await probe_network("www.google.com", 443)
    config = get_config(mode)
    print(f"Config: Timeout={config.timeout}s, Retries={config.retries}, TCP_NODELAY={config.tcp_nodelay}")

if __name__ == "__main__":
    asyncio.run(main())
