"""Tracing utilities submodule.

This submodule provides execution tracing capabilities including call
tracing, performance measurement, and distributed tracing support.
"""

from __future__ import annotations

try:
    from pydvlp.debug.tracing.execution import ExecutionTrace
except ImportError:
    from pydvlp.debug.fallbacks import FallbackTrace as ExecutionTrace

# Create default trace instance
trace = ExecutionTrace()

__all__ = [
    "ExecutionTrace",
    "trace",
]
