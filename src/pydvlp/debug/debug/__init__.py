"""Debug utilities submodule.

This submodule provides enhanced debugging capabilities including
variable inspection, interactive debugging, and decorators.
"""

from __future__ import annotations

try:
    from pydvlp.debug.enhanced import EnhancedDebug
except ImportError:
    from pydvlp.debug.fallbacks import FallbackDebug as EnhancedDebug

try:
    from pydvlp.debug.decorators import debug_decorators
except ImportError:
    debug_decorators = None

try:
    from pydvlp.debug.inspection import variable_inspector
except ImportError:
    variable_inspector = None

try:
    from pydvlp.debug.interactive import interactive_debugger
except ImportError:
    interactive_debugger = None

# Create default debug instance
debug = EnhancedDebug()

__all__ = [
    "EnhancedDebug",
    "debug",
    "debug_decorators",
    "interactive_debugger",
    "variable_inspector",
]
