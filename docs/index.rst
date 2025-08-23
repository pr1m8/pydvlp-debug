PyDvlp Debug Documentation
==========================

Welcome to PyDvlp Debug, a comprehensive Python development utilities library providing advanced debugging, profiling, logging, and code analysis tools.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   api/index
   examples
   contributing

Overview
--------

PyDvlp Debug provides a unified interface for:

* **Enhanced Debugging** - Drop-in replacement for icecream with rich output
* **Performance Profiling** - Multiple profiler backends with minimal overhead
* **Structured Logging** - Beautiful console output with context tracking
* **Code Analysis** - Complexity metrics, type coverage, and static analysis
* **Execution Tracing** - Function call tracking and flow visualization
* **Benchmarking** - Timing, load testing, and performance comparison

Quick Example
-------------

.. code-block:: python

   from pydvlp.debug import debugkit

   # Enhanced debugging
   debugkit.ice("Debug info", value=42)

   # Comprehensive instrumentation
   @debugkit.instrument(analyze=True, profile=True)
   def my_function(data: list[str]) -> dict[str, int]:
       return process_data(data)

   # Code analysis
   report = debugkit.analyze_code(my_function)
   print(f"Complexity: {report.complexity_score}")

Installation
------------

.. code-block:: bash

   pip install pydvlp-debug

Or using PDM:

.. code-block:: bash

   pdm add pydvlp-debug

Features
--------

Enhanced Debugging
~~~~~~~~~~~~~~~~~~

- Icecream-compatible interface with enhancements
- Rich console output with syntax highlighting
- Context-aware debugging information
- Multiple debugger backends (pdb, web-pdb, pudb)

Performance Profiling
~~~~~~~~~~~~~~~~~~~~~

- CPU profiling (cProfile, line_profiler)
- Memory profiling (memory_profiler, tracemalloc)
- Statistical profiling (pyinstrument, py-spy)
- Minimal overhead with sampling support

Structured Logging
~~~~~~~~~~~~~~~~~~

- Rich integration for beautiful output
- JSON-structured logging support
- Context management and correlation
- Performance metrics logging

Code Analysis
~~~~~~~~~~~~~

- Cyclomatic and cognitive complexity
- Halstead metrics
- Type coverage analysis
- Static analysis orchestration

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
