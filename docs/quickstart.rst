Quick Start Guide
=================

This guide will help you get started with PyDvlp Debug quickly.

Installation
------------

Install PyDvlp Debug using pip:

.. code-block:: bash

   pip install pydvlp-debug

Basic Usage
-----------

Enhanced Debugging
~~~~~~~~~~~~~~~~~~

The simplest way to use PyDvlp Debug is through the enhanced debugging interface:

.. code-block:: python

   from pydvlp.debug import debugkit

   # Basic debugging (icecream replacement)
   x = 42
   debugkit.ice(x)  # Output: x: 42

   # With labels
   debugkit.ice(x, "The answer")  # Output: The answer: x: 42

   # Multiple values
   y = "hello"
   debugkit.ice(x, y)  # Output: x: 42, y: 'hello'

Using Individual Components
---------------------------

You can also use individual components directly:

.. code-block:: python

   from pydvlp.debug import debug, log, trace, profile

   # Enhanced debugging
   debug.ice("Debug info", data=my_data)

   # Structured logging
   logger = log.get_logger(__name__)
   logger.info("Process started", extra={"user_id": 123})

   # Function tracing
   @trace.calls
   def tracked_function():
       return compute_result()

   # Performance profiling
   @profile.time
   def slow_function():
       return expensive_operation()

Unified Instrumentation
-----------------------

The most powerful feature is unified instrumentation:

.. code-block:: python

   from pydvlp.debug import debugkit

   @debugkit.instrument(
       analyze=True,    # Enable code analysis
       profile=True,    # Enable profiling
       trace=True,      # Enable tracing
       log=True         # Enable logging
   )
   def process_data(items: list[str]) -> dict[str, int]:
       """Process items and return counts."""
       counts = {}
       for item in items:
           counts[item] = counts.get(item, 0) + 1
       return counts

   # Call the instrumented function
   result = process_data(["apple", "banana", "apple"])

   # Access analysis results
   if hasattr(process_data, '_analysis_report'):
       report = process_data._analysis_report
       print(f"Complexity: {report.complexity_score}")
       print(f"Type coverage: {report.type_coverage:.1%}")

Context Management
------------------

Use context managers for scoped operations:

.. code-block:: python

   from pydvlp.debug import debugkit

   # Create a development context
   with debugkit.create_context("data_processing") as ctx:
       ctx.log("Starting processing")

       # All operations within context are tracked
       result = process_large_dataset()

       ctx.log("Processing complete", extra={"records": len(result)})

   # Context automatically cleaned up

Code Analysis
-------------

Analyze code quality and complexity:

.. code-block:: python

   from pydvlp.debug import debugkit
   from pathlib import Path

   # Analyze a specific function
   def complex_function(data):
       # ... implementation ...
       pass

   report = debugkit.analyze_code(complex_function)
   print(f"Complexity score: {report.complexity_score}")
   print(f"Issues: {report.issues}")
   print(f"Suggestions: {report.suggestions}")

   # Analyze a whole file
   file_report = debugkit.analyze_code(Path("my_module.py"))
   file_report.display()

Performance Profiling
---------------------

Profile function performance:

.. code-block:: python

   from pydvlp.debug import profile_performance

   # As a decorator
   @profile_performance(profiler="line_profiler")
   def compute_heavy():
       result = 0
       for i in range(1000000):
           result += i ** 2
       return result

   # As a context manager
   with profile_performance() as profiler:
       data = load_large_dataset()
       processed = transform_data(data)
       save_results(processed)

Configuration
-------------

Configure PyDvlp Debug behavior:

.. code-block:: python

   from pydvlp.debug import debugkit

   # Configure globally
   debugkit.configure(
       debug_enabled=True,
       profile_enabled=False,  # Disable profiling
       log_level="INFO",
       verbose=True
   )

   # Or use environment variables
   # export PYDVLP_ENV=production
   # export PYDVLP_DEBUG_ENABLED=false
   # export PYDVLP_LOG_LEVEL=WARNING

Next Steps
----------

- Read the :doc:`api/index` for detailed API documentation
- Check out :doc:`examples` for more usage examples
- See :doc:`contributing` to contribute to the project
