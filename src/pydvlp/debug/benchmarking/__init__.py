"""Benchmarking utilities submodule.

This submodule provides benchmarking and performance measurement
capabilities including timing, load testing, and comparison utilities.
"""

from __future__ import annotations

try:
    from pydvlp.debug.benchmarking.core import BenchmarkSuite
    from pydvlp.debug.benchmarking.load import LoadTester
    from pydvlp.debug.benchmarking.timing import TimingBenchmark
except ImportError:
    from pydvlp.debug.fallbacks import FallbackBenchmark as BenchmarkSuite

    TimingBenchmark = None
    LoadTester = None

# Create default benchmark instance
benchmark = BenchmarkSuite()

__all__ = [
    "BenchmarkSuite",
    "LoadTester",
    "TimingBenchmark",
    "benchmark",
]
