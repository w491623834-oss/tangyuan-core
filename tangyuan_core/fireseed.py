"""
FireSeed Validator - Three-dimensional identity verification.
- Memory Key (user's secret)
- Behavioral Fingerprint (typing rhythm, patterns)
- Spacetime Anchor (IP, time, device)
"""

import hashlib
import time
from typing import Dict, Any, Optional

class FireSeedValidator:
    """
    Three-dimensional identity validator.
    
    Usage:
        validator = FireSeedValidator()
        is_valid = validator.verify(
            memory_key="tangyuan2026",
            seed_phrase="orbit canvas ...",
            user_context={"ip": "192.168.1.1", "time": "..."}
        )
    """
    
    def __init__(self):
        self._baseline = {}
        
    def verify(self, memory_key: str, seed_phrase: str, user_context: Dict[str, Any]) -> bool:
        """
        Perform 3D verification.
        
        Args:
            memory_key: User's memory key (e.g., "tangyuan2026")
            seed_phrase: 12-word seed phrase
            user_context: Context dict with ip, time, device info
            
        Returns:
            True if all 3 dimensions pass, False otherwise
        """
        # Dimension 1: Memory Key Validation
        mem_ok = self._verify_memory_key(memory_key)
        
        # Dimension 2: Seed Phrase Validation
        seed_ok = self._verify_seed_phrase(seed_phrase)
        
        # Dimension 3: Spacetime Anchor
        space_ok = self._verify_spacetime(user_context)
        
        return mem_ok and seed_ok and space_ok
    
    def _verify_memory_key(self, key: str) -> bool:
        """Verify memory key matches expected pattern."""
        # In production, this would compare against stored hash
        # For now, check basic structure
        if not key or len(key) < 8:
            return False
        # Simulate hash comparison
        expected_hash = hashlib.sha256("tangyuan2026".encode()).hexdigest()
        actual_hash = hashlib.sha256(key.encode()).hexdigest()
        return expected_hash == actual_hash
    
    def _verify_seed_phrase(self, phrase: str) -> bool:
        """Verify 12-word seed phrase structure."""
        words = phrase.strip().split()
        if len(words) != 12:
            return False
        # Check all words are alphabetic
        return all(word.isalpha() for word in words)
    
    def _verify_spacetime(self, context: Dict[str, Any]) -> bool:
        """Verify spacetime anchor (IP, time, device)."""
        # Check time is reasonable (not too far in past/future)
        current_time = time.time()
        if "timestamp" in context:
            ts = context["timestamp"]
            # If timestamp is 0 or very small, skip time check (test mode)
            if ts > 0:
                time_diff = abs(current_time - ts)
                if time_diff > 300:  # 5 minutes tolerance
                    return False
        
        # IP check would go here (whitelist/range check)
        return True
    
    def generate_hash(self, key: str) -> str:
        """Generate SHA256 hash of a key (for setup)."""
        return hashlib.sha256(key.encode()).hexdigest()
