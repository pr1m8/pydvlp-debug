# Contributing to PyDvlp Debug

We welcome contributions to PyDvlp Debug! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Release Process](#release-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PDM (Python Dependency Manager)
- Git

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/pydvlp-debug.git
cd pydvlp-debug
```

## Development Setup

### 1. Install PDM

If you don't have PDM installed:

```bash
curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
```

### 2. Install Dependencies

```bash
# Install all dependencies including development ones
pdm install -d

# Or install specific groups
pdm install -G dev,test,docs
```

### 3. Set up Pre-commit Hooks

```bash
pdm run pre-commit install
```

### 4. Verify Installation

```bash
# Run tests to ensure everything works
pdm run pytest

# Run type checking
pdm run mypy src/

# Run linting
pdm run ruff check src/
```

## Making Changes

### 1. Create a Branch

Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
# or
git checkout -b docs/documentation-update
```

### 2. Development Guidelines

#### Code Style

- **Python**: Follow PEP 8
- **Line Length**: Maximum 88 characters
- **Imports**: Use isort for import organization
- **Formatting**: Use Black for code formatting

#### Type Hints

All functions must have type hints:

```python
def process_data(items: List[Dict[str, Any]], config: Optional[Config] = None) -> ProcessResult:
    """Process data items according to configuration."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def analyze_function(func: Callable) -> AnalysisReport:
    """Analyze a function for complexity and type coverage.

    Args:
        func: The function to analyze

    Returns:
        AnalysisReport: Complete analysis results including complexity,
            type coverage, and recommendations

    Raises:
        ValueError: If function cannot be analyzed
        TypeError: If input is not a callable

    Examples:
        Analyze a simple function::

            def greet(name: str) -> str:
                return f"Hello, {name}!"

            report = analyze_function(greet)
            print(f"Complexity: {report.complexity_score}")
    """
```

#### Error Handling

- Use specific exception types
- Provide clear error messages
- Include context in error messages:

```python
try:
    result = process_data(data)
except ValueError as e:
    logger.error(f"Failed to process data: {e}", extra={"data_size": len(data)})
    raise ProcessingError(f"Data processing failed: {e}") from e
```

### 3. Commit Messages

Use conventional commits:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Build/tooling changes

Examples:

```
feat: add code complexity analysis
fix: resolve memory leak in profiler
docs: update installation instructions
test: add benchmarking test cases
```

## Testing

### Running Tests

```bash
# Run all tests
pdm run pytest

# Run with coverage
pdm run pytest --cov=pydvlp.debug --cov-report=html

# Run specific test file
pdm run pytest tests/test_profiling.py

# Run with verbose output
pdm run pytest -v

# Run only failed tests
pdm run pytest --lf
```

### Writing Tests

#### Test Structure

Place tests in the `tests/` directory with the naming pattern `test_*.py`:

```
tests/
├── test_core_unified.py
├── test_profiling.py
├── test_analysis.py
└── conftest.py
```

#### Test Examples

```python
import pytest
from pydvlp.debug import debugkit


class TestUnifiedDev:
    """Test suite for UnifiedDev class."""

    def test_basic_functionality(self):
        """Test basic functionality."""
        # Given
        unified = UnifiedDev()

        # When
        result = unified.ice("test")

        # Then
        assert result == "test"

    def test_error_conditions(self):
        """Test error handling."""
        unified = UnifiedDev()

        with pytest.raises(ValueError, match="Invalid input"):
            unified.analyze_code("not a function")

    @pytest.fixture
    def sample_data(self):
        """Provide sample data for tests."""
        return [1, 2, 3, 4, 5]

    def test_with_fixture(self, sample_data):
        """Test using fixture data."""
        assert len(sample_data) == 5
```

#### Test Categories

- **Unit Tests**: Test individual functions/methods
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete workflows
- **Performance Tests**: Test performance characteristics

#### Mocking

Use unittest.mock for external dependencies:

```python
from unittest.mock import patch, MagicMock

def test_with_mock():
    """Test with mocked dependencies."""
    with patch('pydvlp.debug.analysis.mypy_check') as mock_mypy:
        mock_mypy.return_value = MagicMock(errors=[])

        report = analyze_code(test_function)

        assert mock_mypy.called
        assert report.type_errors == []
```

## Documentation

### Types of Documentation

1. **API Documentation**: Docstrings in code
2. **User Guides**: Markdown files in `docs/guides/`
3. **Examples**: Working code in `examples/`
4. **README**: Project overview and quick start

### Building Documentation

```bash
# Install documentation dependencies
pdm install -G docs

# Build documentation locally
pdm run sphinx-build -b html docs/ docs/_build/

# Serve documentation
pdm run python -m http.server -d docs/_build/
```

### Documentation Guidelines

- Keep examples up-to-date with API changes
- Include code examples in docstrings
- Use clear, concise language
- Test code examples to ensure they work

## Submitting Changes

### 1. Before Submitting

Run the full test suite:

```bash
# Format code
pdm run black src/ tests/
pdm run isort src/ tests/

# Type check
pdm run mypy src/

# Lint code
pdm run ruff check src/ tests/

# Run tests
pdm run pytest --cov=pydvlp.debug

# Check documentation
pdm run sphinx-build -b html docs/ docs/_build/
```

### 2. Create Pull Request

1. Push your changes to your fork:

```bash
git push origin feature/your-feature-name
```

2. Create a Pull Request on GitHub
3. Fill out the PR template completely
4. Link any related issues

### 3. Pull Request Template

```markdown
## Description

Brief description of changes made.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing

- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Coverage maintained or improved

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### 4. Review Process

- All PRs require at least one review
- Address feedback promptly
- Keep PRs focused and atomic
- Be responsive to maintainer requests

## Release Process

### Versioning

We use Semantic Versioning (SemVer):

- **MAJOR**: Incompatible API changes
- **MINOR**: Backwards-compatible functionality additions
- **PATCH**: Backwards-compatible bug fixes

### Release Steps (for maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create release tag
4. Build and publish to PyPI
5. Create GitHub release

## Development Guidelines

### Architecture Principles

1. **Modularity**: Each module should have a single responsibility
2. **Fallback Support**: Graceful degradation when dependencies are missing
3. **Performance**: Minimal overhead in production
4. **Extensibility**: Easy to add new analysis tools
5. **Configuration**: Everything should be configurable

### Adding New Features

#### 1. Analysis Tools

To add a new analysis tool:

```python
# src/pydvlp/debug/analysis/your_tool.py
class YourAnalyzer:
    """Your custom analyzer."""

    def analyze_function(self, func: Callable) -> YourReport:
        """Analyze function with your tool."""
        pass

# Register in src/pydvlp/debug/analysis/__init__.py
from .your_tool import YourAnalyzer

def get_your_analyzer() -> YourAnalyzer:
    """Get your analyzer instance."""
    global _your_analyzer
    if _your_analyzer is None:
        _your_analyzer = YourAnalyzer()
    return _your_analyzer
```

#### 2. Profiling Tools

To add a new profiling tool:

```python
# src/pydvlp/debug/profiling/your_profiler.py
class YourProfiler:
    """Your custom profiler."""

    def profile_function(self, func: Callable) -> ProfileResult:
        """Profile function execution."""
        pass
```

#### 3. Configuration Options

Add new configuration options in `DevConfig`:

```python
# src/pydvlp/debug/config.py
class DevConfig:
    def __init__(self):
        self.your_feature_enabled: bool = self._get_bool("PYDVLP_YOUR_FEATURE_ENABLED", True)
```

### Common Patterns

#### Lazy Loading

Use lazy loading for expensive imports:

```python
def get_analyzer():
    """Get analyzer with lazy loading."""
    global _analyzer
    if _analyzer is None:
        try:
            from expensive_library import ExpensiveAnalyzer
            _analyzer = ExpensiveAnalyzer()
        except ImportError:
            from .fallbacks import FallbackAnalyzer
            _analyzer = FallbackAnalyzer()
    return _analyzer
```

#### Fallback Implementation

Always provide fallback implementations:

```python
# fallbacks.py
class FallbackProfiler:
    """Fallback profiler when advanced profiling is unavailable."""

    def profile_function(self, func):
        """Simple profiling using time.time()."""
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end = time.time()
                print(f"PROFILE: {func.__name__} took {end - start:.3f}s")

        return wrapper
```

## Getting Help

- **Documentation**: Check the `docs/` directory
- **Examples**: Look at the `examples/` directory
- **Issues**: Search existing issues on GitHub
- **Discussions**: Use GitHub Discussions for questions

## Recognition

Contributors will be recognized in:

- `CONTRIBUTORS.md` file
- Release notes
- Documentation acknowledgments

Thank you for contributing to PyDvlp Debug!
