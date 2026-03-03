"""
Self-Analysis Module for tangyuan-core.
Scans own code and logs to find optimization opportunities.
"""
import os
import ast
import time
from pathlib import Path

class SelfAnalyzer:
    def __init__(self):
        self.root = Path(__file__).parent / "tangyuan_core"
        self.issues = []
        print(f"[INFO] Starting self-analysis of {self.root}...")

    def analyze_complexity(self):
        """Check for overly complex functions (Cyclomatic Complexity)."""
        print("  [SCAN] Analyzing code complexity...")
        # 简化版：只检查函数行数
        for py_file in self.root.glob("*.py"):
            with open(py_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                func_name = None
                func_start = 0
                in_func = False
                
                for i, line in enumerate(lines):
                    if line.strip().startswith("def "):
                        if in_func:
                            # Previous function ended
                            func_len = i - func_start
                            if func_len > 50:
                                self.issues.append(f"[WARN] Function {func_name} is {func_len} lines (>50). Consider splitting.")
                        func_name = line.strip().split("(")[0].replace("def ", "")
                        func_start = i
                        in_func = True
                
                if in_func:
                    func_len = len(lines) - func_start
                    if func_len > 50:
                        self.issues.append(f"[WARN] Function {func_name} is {func_len} lines (>50).")

    def analyze_dependencies(self):
        """Check for forbidden imports."""
        print("  [SCAN] Checking dependencies...")
        forbidden = ["requests", "pandas", "numpy", "ccxt"]
        for py_file in self.root.glob("*.py"):
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()
                for lib in forbidden:
                    if f"import {lib}" in content or f"from {lib}" in content:
                        self.issues.append(f"[ERROR] Forbidden library '{lib}' found in {py_file.name}!")

    def analyze_performance_hints(self):
        """Look for performance anti-patterns."""
        print("  [SCAN] Looking for performance hints...")
        # Check for time.sleep in async code (should be asyncio.sleep)
        for py_file in self.root.glob("*.py"):
            with open(py_file, "r", encoding="utf-8") as f:
                content = f.read()
                if "async def" in content and "time.sleep" in content:
                    self.issues.append(f"[WARN] Use 'await asyncio.sleep' instead of 'time.sleep' in async code ({py_file.name}).")

    def generate_report(self):
        print("\n--- Self-Analysis Report ---")
        if not self.issues:
            print("[OK] No obvious issues found. Code looks clean!")
        else:
            for issue in self.issues:
                print(f"  {issue}")
        print("--------------------------\n")
        return self.issues

if __name__ == "__main__":
    analyzer = SelfAnalyzer()
    analyzer.analyze_complexity()
    analyzer.analyze_dependencies()
    analyzer.analyze_performance_hints()
    analyzer.generate_report()
