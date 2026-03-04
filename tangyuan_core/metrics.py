import asyncio
import time
from typing import Dict, Any, List

class TradingMetrics:
    """ lightweight trading metrics collector """
    
    def __init__(self):
        self.trades: List[Dict] = []
        self.start_time = time.time()
        
    def record_trade(self, symbol: str, side: str, price: float, qty: float, pnl: float = 0):
        """Record a trade with minimal memory overhead"""
        self.trades.append({
            't': time.time() - self.start_time,  # relative time
            's': symbol,  # symbol
            'd': side[0].upper(),  # B/S
            'p': round(price, 4),
            'q': round(qty, 6),
            'pnl': round(pnl, 4) if pnl else 0
        })
        
    def get_stats(self) -> Dict[str, Any]:
        """Calculate trading statistics"""
        if not self.trades:
            return {'trades': 0, 'win_rate': 0, 'pnl': 0}
            
        winning_trades = [t for t in self.trades if t.get('pnl', 0) > 0]
        total_pnl = sum(t.get('pnl', 0) for t in self.trades)
        
        return {
            'trades': len(self.trades),
            'win_rate': len(winning_trades) / len(self.trades) if self.trades else 0,
            'total_pnl': round(total_pnl, 4),
            'avg_pnl': round(total_pnl / len(self.trades), 4) if self.trades else 0
        }

# Example usage
async def demo():
    metrics = TradingMetrics()
    
    # Simulate trades
    metrics.record_trade('ETH-USDT', 'buy', 3500.50, 0.1)
    await asyncio.sleep(1)
    metrics.record_trade('ETH-USDT', 'sell', 3510.00, 0.1, 0.95)
    
    stats = metrics.get_stats()
    print(f"Stats: {stats}")

if __name__ == "__main__":
    asyncio.run(demo())
