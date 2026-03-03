"""
TY-RAL: TangYuan Runtime Abstraction Layer.
Provides cross-platform compatibility (Win/Mac/Linux) for file paths, encoding, etc.
"""

import os
import sys
import platform

class RAL:
    """
    Runtime Abstraction Layer for cross-platform compatibility.
    """
    
    def __init__(self):
        self.os_type = self._detect_os()
        self.encoding = "utf-8"
        
    def _detect_os(self) -> str:
        """Detect operating system."""
        system = platform.system().lower()
        if system == "windows":
            return "windows"
        elif system == "darwin":
            return "macos"
        else:
            return "linux"
    
    def get_line_ending(self) -> str:
        """Get OS-specific line ending."""
        if self.os_type == "windows":
            return "\r\n"
        return "\n"
    
    def normalize_path(self, path: str) -> str:
        """Normalize path for current OS."""
        return os.path.normpath(path)
    
    def is_valid_script_encoding(self, content: str) -> bool:
        """
        Check if content is safe for PowerShell 5.1 (ASCII only).
        Returns True if safe, False if contains forbidden chars.
        """
        try:
            content.encode('ascii')
            return True
        except UnicodeEncodeError:
            return False
    
    def sanitize_for_script(self, content: str) -> str:
        """
        Sanitize content for PowerShell scripts (remove emoji, unicode).
        Replaces forbidden chars with ASCII equivalents.
        """
        # Remove emoji and non-ASCII
        sanitized = ""
        for char in content:
            if ord(char) < 128:  # ASCII only
                sanitized += char
            else:
                # Replace common patterns
                if char in ["✅", "✓"]:
                    sanitized += "[OK]"
                elif char in ["❌", "✗"]:
                    sanitized += "[FAIL]"
                elif char in ["⚠️"]:
                    sanitized += "[WARN]"
                else:
                    sanitized += "?"
        return sanitized
    
    def get_config_dir(self, app_name: str) -> str:
        """Get platform-specific config directory."""
        if self.os_type == "windows":
            return os.path.join(os.getenv("APPDATA", ""), app_name)
        elif self.os_type == "macos":
            return os.path.expanduser(f"~/Library/Application Support/{app_name}")
        else:
            return os.path.expanduser(f"~/.config/{app_name}")

# Global instance
ral = RAL()
