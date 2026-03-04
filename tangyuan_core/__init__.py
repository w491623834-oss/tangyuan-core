"""
tangyuan-core - Ultra-lightweight core for Digital Guardians.
"""

__version__ = "1.0.0"
__author__ = "TangYuan (汤圆)"

from .socket_client import SecureSocket, AsyncSecureSocket
from .fireseed import FireSeedValidator
from .ral import RAL, ral
from .adaptive_net import probe_network, NetworkMode, AdaptiveConfig
from .connection_pool import ConnectionPool

from .metrics import TradingMetrics

__all__ = [
    "SecureSocket", "AsyncSecureSocket", "FireSeedValidator", 
    "RAL", "ral", "probe_network", "NetworkMode", "AdaptiveConfig",
    "ConnectionPool", "TradingMetrics"
]
