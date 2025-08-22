"""Unified development utilities for Python debugging, profiling, and analysis.

This package provides a comprehensive suite of development tools including:
- Enhanced debugging with multiple debugger integrations
- Rich logging with structured output and context management
- Advanced code tracing and execution analysis
- Performance profiling with multiple profiler backends
- Comprehensive static analysis orchestration
- Code complexity and type analysis
- Benchmarking and load testing utilities

All utilities are designed to work together seamlessly and provide
both simple interfaces for quick debugging and advanced features
for comprehensive code analysis.

Examples:
    Quick start with unified interface::

        from pydvlp.debug import debugkit

        # Enhanced debugging
        debugkit.ice("Debug variable", value=42)

        # Rich logging with context
        with debugkit.context("operation") as ctx:
            ctx.log("Starting process")
            # ... work ...
            ctx.log("Process complete")

        # Complete analysis
        @debugkit.instrument(analyze=True, profile=True)
        def my_function(data: List[str]) -> Dict[str, int]:
            return process_data(data)

    Individual component usage::

        from pydvlp.debug import debug, log, trace, profile

        # Use specific components
        debug.ice("Variable inspection", data=my_data)
        log.info("Process started", context={"user": "alice"})

        @trace.calls
        @profile.time
        def traced_function():
            return complex_operation()

    Advanced analysis::

        from pydvlp.debug import debugkit

        # Analyze code quality
        analysis = debugkit.analyze_code(my_function)
        print(f"Type coverage: {analysis.type_analysis.type_coverage:.1%}")
        print(f"Complexity grade: {analysis.complexity_analysis.complexity_grade}")

        # Run static analysis
        results = debugkit.static_analysis.analyze_file(Path("module.py"))
        report = debugkit.static_analysis.generate_report(results)
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydvlp.debug import debug
from pydvlp.debug.benchmarking import benchmark
from pydvlp.debug.config import DevConfig, Environment, LogLevel, StorageBackend, config
from pydvlp.debug.core import CodeAnalysisReport, DevContext, UnifiedDev
from pydvlp.debug.logging import log
from pydvlp.debug.profiling import profile
from pydvlp.debug.tracing import trace

# Analysis components
# Core configuration
# Core components
# Individual component interfaces with fallbacks

if TYPE_CHECKING:
    pass


# Create global instance
debugkit = UnifiedDev()

# Export main interface and individual components
__all__ = [
    "CodeAnalysisReport",
    "DevConfig",
    "DevContext",
    "Environment",
    "LogLevel",
    "StorageBackend",
    "UnifiedDev",
    "benchmark",
    "config",
    "debug",
    "debugkit",
    "log",
    "profile",
    "trace",
]
