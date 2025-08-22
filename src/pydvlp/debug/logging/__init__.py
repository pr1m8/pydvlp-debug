"""Logging utilities submodule.

This submodule provides structured logging capabilities with correlation
IDs, context management, and rich output formatting.
"""

from __future__ import annotations

try:
    from pydvlp.debug.logging.structured import StructuredLog
except ImportError:
    from pydvlp.debug.fallbacks import FallbackLog as StructuredLog

# Create default log instance
log = StructuredLog()

__all__ = [
    "StructuredLog",
    "log",
]
