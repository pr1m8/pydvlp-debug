"""Profiling utilities submodule.

This submodule provides performance profiling capabilities including CPU
profiling, memory profiling, and statistical analysis.
"""

from __future__ import annotations

try:
    from pydvlp.debug.profiling.performance import PerformanceProfiler
except ImportError:
    from pydvlp.debug.fallbacks import FallbackProfile as PerformanceProfiler

# Create default profile instance
profile = PerformanceProfiler()

__all__ = [
    "PerformanceProfiler",
    "profile",
]
