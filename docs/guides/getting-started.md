# Getting Started

Welcome to PyDvlp Debug! This guide will help you start using our Python development utilities in minutes.

## Quick Install

```bash
pip install pydvlp-debug
```

## First Example

```python
from pydvlp.debug import debugkit

# Debug any value
x = 42
debugkit.ice(x)  # Shows: x = 42

# Debug multiple values
name = "Alice"
debugkit.ice(name, x)  # Shows: name = 'Alice', x = 42
```

## Core Features

### 1. Smart Debugging

```python
# Debug complex objects
data = {"users": [{"name": "Alice", "age": 30}]}
debugkit.ice(data)

# Debug with context
debugkit.ice("Processing user", id=123, status="active")
```

### 2. Performance Profiling

```python
# Profile any function
@debugkit.instrument(profile=True)
def slow_function():
    time.sleep(0.1)
    return "done"

result = slow_function()
# Shows: slow_function took 0.1s
```

### 3. Code Analysis

```python
# Analyze code quality
def messy_function(x, y, z=None):
    if x > 0:
        if y > 0:
            return x + y
    return 0

report = debugkit.analyze_code(messy_function)
print(f"Code quality: {report.combined_score}/100")
```

## Common Patterns

### Development Workflow

```python
# Configure for development
debugkit.configure(
    debug_enabled=True,
    profile_enabled=True,
    log_level="DEBUG"
)

# Use context for operations
with debugkit.context("user_signup") as ctx:
    ctx.debug("Validating email")
    # ... your code ...
    ctx.success("User created")
```

### Production Mode

```python
# Set production environment
import os
os.environ["PYDVLP_ENVIRONMENT"] = "production"

from pydvlp.debug import debugkit
# Automatically optimized - only errors logged
```

## Installation Options

### Basic Install
```bash
pip install pydvlp-debug
```

### With Extra Features
```bash
# Rich console output
pip install "pydvlp-debug[rich]"

# All features
pip install "pydvlp-debug[all]"
```

## Next Steps

- [Configuration Guide](configuration.md) - Customize PyDvlp Debug
- [API Reference](../api/index.md) - Detailed documentation
- [Best Practices](best-practices.md) - Tips and patterns

## Need Help?

- 📖 Check our [examples](https://github.com/pr1m8/pydvlp-debug/tree/main/examples)
- 🐛 Report issues on [GitHub](https://github.com/pr1m8/pydvlp-debug/issues)
- 💬 Ask questions in [Discussions](https://github.com/pr1m8/pydvlp-debug/discussions)