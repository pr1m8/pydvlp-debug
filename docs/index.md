# PyDvlp Debug

Professional Python development utilities for debugging, profiling, and code analysis.

## What is PyDvlp Debug?

PyDvlp Debug is a **zero-dependency** Python library that enhances your development workflow with powerful debugging, profiling, and analysis tools. It works out of the box with Python's standard library, and gets even better with optional dependencies.

## Key Features

✨ **Smart Debugging** - Ice-cream style debug output that shows variable names and values  
⚡ **Performance Profiling** - Time and memory profiling with minimal overhead  
🔍 **Code Analysis** - Complexity metrics, type coverage, and quality scoring  
📊 **Production Ready** - Automatic optimization based on environment  
🎯 **Zero Dependencies** - Core features work without any external packages

## Quick Example

```python
from pydvlp.debug import debugkit

# Enhanced debugging
x = 42
debugkit.ice(x)  # Output: x = 42

# Profile performance
@debugkit.instrument(profile=True)
def calculate():
    return sum(range(1000000))

# Analyze code quality
report = debugkit.analyze_code(calculate)
print(f"Code quality: {report.combined_score}/100")
```

## Get Started in 30 Seconds

```bash
pip install pydvlp-debug
```

```python
from pydvlp.debug import debugkit

# Start debugging immediately
debugkit.ice("Hello PyDvlp Debug!")
```

## Learn More

<div class="grid cards" markdown>

- **[Getting Started](guides/getting-started.md)**  
  Installation and first steps

- **[API Reference](api/index.md)**  
  Complete API documentation

- **[Configuration](guides/configuration.md)**  
  Customize behavior and settings

- **[Best Practices](guides/best-practices.md)**  
  Tips for effective usage

</div>

## Why PyDvlp Debug?

- **Works Everywhere** - No required dependencies means it works in any Python environment
- **Production Safe** - Automatically disables expensive operations in production
- **Comprehensive** - Everything you need for debugging, profiling, and analysis in one package
- **Fast** - Minimal overhead when disabled, efficient when enabled

## Community

- 📖 [Documentation](https://pydvlp-debug.readthedocs.io)
- 💻 [Source Code](https://github.com/pr1m8/pydvlp-debug)
- 🐛 [Issue Tracker](https://github.com/pr1m8/pydvlp-debug/issues)
- 💬 [Discussions](https://github.com/pr1m8/pydvlp-debug/discussions)

---

Made with ❤️ by [William R. Astley](https://github.com/pr1m8)