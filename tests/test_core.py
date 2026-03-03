"""
Test suite for tangyuan-core.
Run with: pytest tests/
"""

import pytest
import sys
import os
import asyncio

# Add parent dir to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tangyuan_core.fireseed import FireSeedValidator
from tangyuan_core.ral import RAL
from tangyuan_core.socket_client import AsyncSecureSocket

class TestFireSeedValidator:
    def test_valid_memory_key(self):
        validator = FireSeedValidator()
        # Correct key should pass
        assert validator._verify_memory_key("tangyuan2026") == True
    
    def test_invalid_memory_key(self):
        validator = FireSeedValidator()
        # Wrong key should fail
        assert validator._verify_memory_key("wrong_key") == False
    
    def test_valid_seed_phrase(self):
        validator = FireSeedValidator()
        phrase = "orbit canvas friction galaxy whisper bronze silent thunder puzzle harvest echo tangyuan"
        assert validator._verify_seed_phrase(phrase) == True
    
    def test_invalid_seed_phrase_length(self):
        validator = FireSeedValidator()
        # Wrong word count
        assert validator._verify_seed_phrase("orbit canvas friction") == False
    
    def test_full_verification(self):
        validator = FireSeedValidator()
        result = validator.verify(
            memory_key="tangyuan2026",
            seed_phrase="orbit canvas friction galaxy whisper bronze silent thunder puzzle harvest echo tangyuan",
            user_context={"timestamp": 0}  # Skip time check
        )
        assert result == True

class TestRAL:
    def test_detect_os(self):
        ral = RAL()
        assert ral.os_type in ["windows", "macos", "linux"]
    
    def test_line_ending(self):
        ral = RAL()
        ending = ral.get_line_ending()
        assert ending in ["\r\n", "\n"]
    
    def test_ascii_check(self):
        ral = RAL()
        assert ral.is_valid_script_encoding("hello world") == True
        assert ral.is_valid_script_encoding("你好") == False
    
    def test_sanitize(self):
        ral = RAL()
        result = ral.sanitize_for_script("Hello ✅ World ❌")
        assert "✅" not in result
        assert "[OK]" in result

class TestAsyncSocket:
    """Test async socket creation (without actual connection)."""
    
    def test_async_socket_init(self):
        client = AsyncSecureSocket("example.com", 443)
        assert client.host == "example.com"
        assert client.port == 443
        assert client.use_ssl == True
    
    def test_sync_wrapper_init(self):
        from tangyuan_core.socket_client import SecureSocket
        client = SecureSocket("example.com", 443)
        assert client.host == "example.com"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
