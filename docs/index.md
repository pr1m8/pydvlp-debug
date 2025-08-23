# PyDvlp Debug Documentation

Welcome to the complete documentation for PyDvlp Debug, a comprehensive Python development utilities library.

## Quick Navigation

### Getting Started

- [Installation & Quick Start](https://github.com/pr1m8/pydvlp-debug#quick-start) - Get up and running quickly
- [Getting Started Guide](guides/getting-started.md) - Comprehensive introduction
- [Configuration Guide](guides/configuration.md) - Setup and configuration options
- [Best Practices](guides/best-practices.md) - Development guidelines and patterns

### API Reference

- [Core API](api/core.md) - UnifiedDev, DevContext, and main interfaces
- [Debugging API](api/debugging.md) - Enhanced debugging with ice() and variable inspection
- [Profiling API](api/profiling.md) - Performance and memory profiling tools
- [Analysis API](api/analysis.md) - Code analysis, complexity, and quality metrics

### Examples

- [Basic Debugging](https://github.com/pr1m8/pydvlp-debug/blob/main/examples/basic_debugging.py) - Variable inspection and debugging patterns
- [Performance Profiling](https://github.com/pr1m8/pydvlp-debug/blob/main/examples/performance_profiling.py) - Profiling and optimization workflows
- [Code Analysis](https://github.com/pr1m8/pydvlp-debug/blob/main/examples/code_analysis.py) - Quality assessment and improvement
- [Benchmarking](https://github.com/pr1m8/pydvlp-debug/blob/main/examples/benchmarking.py) - Performance comparison techniques

### Development

- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute to the project
- [Changelog](CHANGELOG.md) - Version history and release notes

## What is PyDvlp Debug?

PyDvlp Debug is a comprehensive Python development utilities library that provides:

- **🐛 Enhanced Debugging** - Advanced variable inspection with `ice()` style debugging
- **📊 Performance Profiling** - Memory and time profiling with decorators and context managers
- **🔍 Execution Tracing** - Detailed execution flow tracking with call graphs
- **⚡ Benchmarking** - Microbenchmark utilities with statistical analysis
- **📝 Structured Logging** - Rich, context-aware logging with multiple handlers
- **🔬 Code Analysis** - Type checking, complexity analysis, and code quality metrics
- **🎯 Zero Dependencies** - Graceful fallbacks when optional dependencies are missing
- **🔧 Unified Interface** - Single entry point for all development tools

## Architecture Overview

```
PyDvlp Debug Architecture
├── Core
│   ├── UnifiedDev (Main Interface)
│   ├── DevContext (Context Management)
│   └── Configuration System
├── Modules
│   ├── Debug (Variable Inspection)
│   ├── Profile (Performance Analysis)
│   ├── Trace (Execution Tracking)
│   ├── Benchmark (Performance Comparison)
│   ├── Log (Structured Logging)
│   └── Analysis (Code Quality)
└── Fallbacks
    └── Zero-dependency implementations
```

## Key Features

### Unified Interface

Single entry point for all development utilities:

```python
from pydvlp.debug import debugkit

# Enhanced debugging
debugkit.ice("Debug info", variable=value)

# Context management
with debugkit.context("operation") as ctx:
    ctx.debug("Starting")
    result = do_work()
    ctx.success("Complete")

# Function instrumentation
@debugkit.instrument(profile=True, analyze=True)
def my_function():
    return "result"
```

### Environment Awareness

Automatically optimizes for different environments:

```python
# Development: Full debugging, profiling, analysis
# Testing: Minimal overhead, focused on test results
# Production: Error logging only, zero overhead
```

### Zero Dependencies

Works without any optional packages:

```python
# Always works, regardless of installed packages
from pydvlp.debug import debug
debug.ice("Hello world!")  # ✅ Always works
```

## Module Overview

### Core Modules

| Module        | Purpose                | Key Features                                            |
| ------------- | ---------------------- | ------------------------------------------------------- |
| **debugkit**  | Unified interface      | Single entry point, context management, instrumentation |
| **debug**     | Variable inspection    | Ice-cream style debugging, automatic variable detection |
| **profile**   | Performance analysis   | Time/memory profiling, decorators, context managers     |
| **trace**     | Execution tracking     | Call graphs, correlation IDs, sampling                  |
| **benchmark** | Performance comparison | Statistical analysis, comparative benchmarks            |
| **log**       | Structured logging     | Rich output, JSON format, context awareness             |

### Analysis Modules

| Module                  | Purpose            | Key Features                                    |
| ----------------------- | ------------------ | ----------------------------------------------- |
| **analysis.types**      | Type analysis      | Type coverage, safety scoring, mypy integration |
| **analysis.complexity** | Complexity metrics | Cyclomatic, cognitive, Halstead complexity      |
| **analysis.static**     | Static analysis    | Multi-tool orchestration, quality scoring       |

## Use Cases

### Development Debugging

```python
from pydvlp.debug import debug

# Quick variable inspection
data = {"users": [1, 2, 3], "total": 100}
debug.ice("Processing", data=data, status="active")
```

### Performance Optimization

```python
from pydvlp.debug import profile, benchmark

@profile.profile_performance
def slow_function():
    return expensive_operation()

# Compare implementations
benchmark.compare(old_impl, new_impl, test_data)
```

### Code Quality Assessment

```python
from pydvlp.debug import debugkit

report = debugkit.analyze_code(my_function)
print(f"Quality score: {report.combined_score}/100")
```

### Production Monitoring

```python
# Automatically optimized for production
@debugkit.instrument(
    profile=debugkit.config.profile_enabled,  # Only if explicitly enabled
    log=True  # Always log in production
)
def api_endpoint(request):
    return process_request(request)
```

## Installation Options

### Basic Installation

```bash
pip install pydvlp-debug
```

### With All Features

```bash
pip install "pydvlp-debug[all]"
```

### Specific Features

```bash
pip install "pydvlp-debug[analysis,profiling,rich]"
```

## Configuration

### Environment Variables

```bash
# Core settings
export PYDVLP_ENVIRONMENT=development
export PYDVLP_ENABLED=true

# Feature toggles
export PYDVLP_DEBUG_ENABLED=true
export PYDVLP_PROFILE_ENABLED=true
export PYDVLP_LOG_LEVEL=INFO
```

### Programmatic

```python
from pydvlp.debug import debugkit

debugkit.configure(
    debug_enabled=True,
    profile_enabled=True,
    log_level="DEBUG"
)
```

## Examples by Use Case

### Debugging Complex Functions

```python
def complex_algorithm(data, options):
    debug.ice("Input", data_size=len(data), options=options)

    with debugkit.context("preprocessing") as ctx:
        processed = preprocess(data)
        ctx.checkpoint("preprocessed", count=len(processed))

    with debugkit.context("analysis") as ctx:
        results = analyze(processed, options)
        ctx.success("Analysis complete", results_count=len(results))

    return results
```

### Performance Benchmarking

```python
# Compare different approaches
@benchmark.measure(iterations=1000)
def approach_a(data):
    return [x for x in data if x > 0]

@benchmark.measure(iterations=1000)
def approach_b(data):
    return list(filter(lambda x: x > 0, data))

# Get comparison report
report = benchmark.get_report()
print(report.summary())
```

### Code Quality Monitoring

```python
def check_code_quality():
    """CI/CD integration for code quality."""
    functions_to_check = [func1, func2, func3]

    for func in functions_to_check:
        report = debugkit.analyze_code(func)

        if report.combined_score < 70:
            print(f"❌ {func.__name__}: Quality too low")
            return False

        if report.complexity_analysis.risk_score > 50:
            print(f"⚠️ {func.__name__}: Too complex")

    print("✅ All functions meet quality standards")
    return True
```

## Support and Community

- **Documentation**: This documentation site
- **Examples**: Working examples in the repository
- **Issues**: GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions
- **Contributing**: See [Contributing Guidelines](CONTRIBUTING.md)

## Version Information

- **Current Version**: 0.1.0
- **Python Support**: 3.8+
- **License**: MIT
- **Changelog**: [Full changelog](CHANGELOG.md)

---

## Quick Links

- [📚 Getting Started](guides/getting-started.md)
- [⚙️ Configuration](guides/configuration.md)
- [🏆 Best Practices](guides/best-practices.md)
- [🔧 API Reference](api/core.md)
- [💡 Examples](https://github.com/pr1m8/pydvlp-debug/tree/main/examples)
- [🤝 Contributing](CONTRIBUTING.md)
