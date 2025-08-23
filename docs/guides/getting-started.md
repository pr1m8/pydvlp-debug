# Getting Started with PyDvlp Debug

This guide will help you get up and running with PyDvlp Debug, a comprehensive Python development utilities library.

## Installation

### Prerequisites

- Python 3.8 or higher
- PDM (recommended) or pip

### Basic Installation

Using PDM (recommended):

```bash
pdm add pydvlp-debug
```

Using pip:

```bash
pip install pydvlp-debug
```

### Installation with Optional Dependencies

For full functionality, install with all optional dependencies:

```bash
# All features
pdm add "pydvlp-debug[all]"

# Specific features
pdm add "pydvlp-debug[analysis]"    # Code analysis tools
pdm add "pydvlp-debug[profiling]"   # Advanced profiling
pdm add "pydvlp-debug[tracing]"     # Execution tracing
pdm add "pydvlp-debug[rich]"        # Rich console output
```

## First Steps

### 1. Import the Library

The main entry point is the `debugkit` object:

```python
from pydvlp.debug import debugkit
```

You can also import specific modules:

```python
from pydvlp.debug import debug, profile, trace, benchmark, log
```

### 2. Basic Debugging

Use the `ice()` method for enhanced debugging output:

```python
from pydvlp.debug import debug

# Debug variables
x = 42
debug.ice(x)  # Output: 🔍 42

# Debug multiple values
name = "Alice"
age = 30
debug.ice(name, age)  # Output: 🔍 'Alice' | 30

# Debug with labels
debug.ice("User info", name=name, age=age)
# Output: 🔍 User info | name='Alice' | age=30
```

### 3. Using the Unified Interface

The `debugkit` object provides a unified interface for all tools:

```python
from pydvlp.debug import debugkit

# Configure settings
debugkit.configure(
    debug_enabled=True,
    profile_enabled=True,
    log_level="INFO"
)

# Use integrated debugging
value = debugkit.ice({"data": [1, 2, 3]})

# Log messages
debugkit.info("Application started")
debugkit.success("Task completed", duration=1.23)
debugkit.error("Connection failed", retry=3)
```

### 4. Context Management

Use contexts to group related operations:

```python
with debugkit.context("user_registration") as ctx:
    ctx.debug("Starting registration")

    # Perform registration steps
    user = create_user(data)
    ctx.checkpoint("user_created")

    send_welcome_email(user)
    ctx.checkpoint("email_sent")

    ctx.success("Registration complete", user_id=user.id)
```

### 5. Function Instrumentation

Automatically add logging, profiling, and analysis to functions:

```python
@debugkit.instrument(profile=True, log=True)
def process_data(items: list) -> dict:
    """Process a list of items."""
    result = {
        "count": len(items),
        "processed": [transform(item) for item in items]
    }
    return result

# The function now automatically logs and profiles
data = process_data([1, 2, 3, 4, 5])
```

## Configuration

### Environment Variables

PyDvlp Debug can be configured using environment variables:

```bash
# Enable/disable features
export PYDVLP_ENABLED=true
export PYDVLP_DEBUG_ENABLED=true
export PYDVLP_PROFILE_ENABLED=false

# Set environment
export PYDVLP_ENVIRONMENT=development  # or testing, production

# Configure logging
export PYDVLP_LOG_LEVEL=INFO
export PYDVLP_LOG_FORMAT=rich  # or json, plain
```

### Programmatic Configuration

Configure at runtime:

```python
from pydvlp.debug import debugkit

debugkit.configure(
    enabled=True,
    debug_enabled=True,
    profile_enabled=True,
    trace_enabled=False,
    log_level="DEBUG",
    environment="development"
)
```

### Production Mode

The library automatically optimizes for production:

```python
import os
os.environ["PYDVLP_ENVIRONMENT"] = "production"

from pydvlp.debug import debugkit
# Automatically configured with:
# - Log level: ERROR
# - Debug/trace/profile: disabled
# - Minimal overhead
```

## Common Use Cases

### 1. Debugging a Complex Function

```python
from pydvlp.debug import debug

def complex_algorithm(data, options):
    debug.ice("Input", data_size=len(data), options=options)

    # Step 1: Preprocessing
    preprocessed = preprocess(data)
    debug.ice("After preprocessing", size=len(preprocessed))

    # Step 2: Main processing
    if options.get('parallel'):
        debug.ice("Using parallel processing")
        result = parallel_process(preprocessed)
    else:
        debug.ice("Using sequential processing")
        result = sequential_process(preprocessed)

    debug.ice("Final result", result_size=len(result))
    return result
```

### 2. Performance Optimization

```python
from pydvlp.debug import profile, benchmark

# Profile to find bottlenecks
@profile.profile_performance
def current_implementation(data):
    # ... existing code ...
    pass

# Benchmark alternatives
@benchmark.measure(iterations=100)
def optimized_version(data):
    # ... optimized code ...
    pass

# Compare results
benchmark.compare(
    current_implementation,
    optimized_version,
    test_data=sample_data
)
```

### 3. Production Debugging

```python
from pydvlp.debug import debugkit

@debugkit.instrument(
    profile=debugkit.config.profile_enabled,  # Controlled by env
    log=True,
    analyze=False  # Don't analyze in production
)
def production_endpoint(request):
    """Production API endpoint with conditional instrumentation."""
    try:
        result = process_request(request)
        debugkit.success("Request processed",
                        request_id=request.id,
                        duration=request.duration)
        return result
    except Exception as e:
        debugkit.error("Request failed",
                      request_id=request.id,
                      error=str(e))
        raise
```

### 4. Code Quality Analysis

```python
from pydvlp.debug import debugkit

def analyze_my_code():
    """Check code quality before committing."""
    functions = [
        process_user_data,
        calculate_metrics,
        generate_report
    ]

    for func in functions:
        report = debugkit.analyze_code(func)
        print(f"\n{func.__name__}:")
        print(f"  Quality Score: {report.combined_score:.1f}/100")
        print(f"  Complexity: {report.complexity_analysis.complexity_grade}")
        print(f"  Type Coverage: {report.type_analysis.type_coverage:.1%}")

        if report.recommendations:
            print("  Recommendations:")
            for rec in report.recommendations[:3]:
                print(f"    - {rec}")
```

## Next Steps

1. **Explore Examples**: Check the `examples/` directory for complete working examples
2. **Read API Docs**: See the [API Reference](../api/) for detailed documentation
3. **Learn Best Practices**: Read the [Best Practices Guide](./best-practices.md)
4. **Configure for Your Needs**: See the [Configuration Guide](./configuration.md)

## Getting Help

- **Documentation**: Check the `docs/` directory
- **Examples**: Look at the `examples/` directory
- **Issues**: Report bugs on GitHub
- **Community**: Join discussions on GitHub Discussions

## Tips for Success

1. **Start Simple**: Begin with basic debugging and gradually add more features
2. **Use Contexts**: Group related operations for better organization
3. **Configure Appropriately**: Different settings for development vs production
4. **Measure Don't Guess**: Use profiling to find actual bottlenecks
5. **Automate Quality**: Add code analysis to your CI/CD pipeline
