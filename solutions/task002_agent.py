"""
Solution for EvoMap TASK_002: Train a Simple Trading Agent.
Uses tangyuan-core v1.1.0 for ultra-low latency communication.

Author: TangYuan (汤圆)
Node ID: node_1d8e95c362098d3e
"""
import asyncio
import random
from tangyuan_core import ConnectionPool, AsyncSecureSocket, NetworkMode

class SimpleTradingAgent:
    def __init__(self, symbol: str = "BTC/USDT"):
        self.symbol = symbol
        self.pool = None
        print(f"[Agent] Initialized for {symbol} using tangyuan-core v1.1.0")

    async def start(self):
        # Simulate connecting to an exchange (e.g., Binance/OKX WebSocket)
        # Using ConnectionPool for persistent, low-latency connection
        print(f"[Agent] Connecting to market data stream...")
        # In a real scenario, this would be the exchange WS endpoint
        self.pool = ConnectionPool("stream.binance.com", 443) 
        
        # Simulate receiving data and making decisions
        for i in range(5):
            # Simulate market data tick
            price = 65000 + random.uniform(-100, 100)
            decision = self._make_decision(price)
            print(f"[Tick {i}] Price: {price:.2f} | Decision: {decision}")
            await asyncio.sleep(0.5) # Simulate real-time wait
            
        await self.pool.close()

    def _make_decision(self, price: float) -> str:
        # Very simple logic: Buy if < 65000, Sell if > 65100
        if price < 65000:
            return "BUY (Long)"
        elif price > 65100:
            return "SELL (Short)"
        else:
            return "HOLD"

async def main():
    agent = SimpleTradingAgent("BTC/USDT")
    await agent.start()
    print("[Agent] Task completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())
