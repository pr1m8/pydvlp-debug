# Configuration Guide

PyDvlp Debug provides flexible configuration options through environment variables, configuration files, and programmatic settings.

## Configuration Methods

### 1. Environment Variables

The most common way to configure PyDvlp Debug is through environment variables:

```bash
# Core settings
export PYDVLP_ENABLED=true
export PYDVLP_ENVIRONMENT=development

# Feature toggles
export PYDVLP_DEBUG_ENABLED=true
export PYDVLP_PROFILE_ENABLED=true
export PYDVLP_TRACE_ENABLED=false
export PYDVLP_BENCHMARK_ENABLED=true

# Logging configuration
export PYDVLP_LOG_ENABLED=true
export PYDVLP_LOG_LEVEL=INFO
export PYDVLP_LOG_FORMAT=rich

# Performance settings
export PYDVLP_TRACE_SAMPLING_RATE=0.1
export PYDVLP_PROFILE_MEMORY=true
export PYDVLP_PROFILE_MIN_DURATION=0.01

# Storage settings
export PYDVLP_STORAGE_BACKEND=sqlite
export PYDVLP_STORAGE_PATH=/tmp/pydvlp.db
```

### 2. Programmatic Configuration

Configure at runtime using the `configure()` method:

```python
from pydvlp.debug import debugkit

debugkit.configure(
    # Core settings
    enabled=True,
    environment="development",

    # Feature toggles
    debug_enabled=True,
    profile_enabled=True,
    trace_enabled=True,
    benchmark_enabled=True,
    log_enabled=True,

    # Logging
    log_level="DEBUG",
    log_format="rich",
    log_use_colors=True,

    # Performance
    trace_sampling_rate=0.5,
    profile_memory=True,
    profile_min_duration=0.001,

    # Analysis
    static_analysis_enabled=True,
    auto_analyze=False,
    strict_thresholds=True
)
```

### 3. Configuration Object

Create and use a custom configuration object:

```python
from pydvlp.debug.config import DevConfig, LogLevel, Environment

# Create custom config
config = DevConfig(
    enabled=True,
    environment=Environment.DEVELOPMENT,
    debug_enabled=True,
    profile_enabled=True,
    log_level=LogLevel.DEBUG,
    trace_sampling_rate=0.1
)

# Use with UnifiedDev
from pydvlp.debug.core.unified import UnifiedDev
debugkit = UnifiedDev(config)
```

## Environment-Specific Settings

### Development Environment

Optimized for debugging and analysis:

```python
# .env.development
PYDVLP_ENVIRONMENT=development
PYDVLP_DEBUG_ENABLED=true
PYDVLP_PROFILE_ENABLED=true
PYDVLP_TRACE_ENABLED=true
PYDVLP_LOG_LEVEL=DEBUG
PYDVLP_LOG_FORMAT=rich
PYDVLP_STATIC_ANALYSIS_ENABLED=true
PYDVLP_AUTO_ANALYZE=true
```

### Testing Environment

Balanced for test execution:

```python
# .env.testing
PYDVLP_ENVIRONMENT=testing
PYDVLP_DEBUG_ENABLED=false
PYDVLP_PROFILE_ENABLED=false
PYDVLP_TRACE_ENABLED=false
PYDVLP_LOG_LEVEL=WARNING
PYDVLP_LOG_FORMAT=plain
PYDVLP_BENCHMARK_ENABLED=true
```

### Production Environment

Minimal overhead and security:

```python
# .env.production
PYDVLP_ENVIRONMENT=production
PYDVLP_ENABLED=true
PYDVLP_DEBUG_ENABLED=false
PYDVLP_PROFILE_ENABLED=false
PYDVLP_TRACE_ENABLED=false
PYDVLP_LOG_LEVEL=ERROR
PYDVLP_LOG_FORMAT=json
PYDVLP_STORAGE_BACKEND=none
```

## Configuration Options Reference

### Core Settings

| Option           | Type | Default         | Description                                       |
| ---------------- | ---- | --------------- | ------------------------------------------------- |
| `enabled`        | bool | `True`          | Master switch for all features                    |
| `environment`    | str  | `"development"` | Environment name (development/testing/production) |
| `correlation_id` | str  | `None`          | Correlation ID for distributed tracing            |

### Feature Toggles

| Option              | Type | Default | Description                  |
| ------------------- | ---- | ------- | ---------------------------- |
| `debug_enabled`     | bool | `True`  | Enable debug output (ice)    |
| `profile_enabled`   | bool | `False` | Enable performance profiling |
| `trace_enabled`     | bool | `False` | Enable execution tracing     |
| `benchmark_enabled` | bool | `True`  | Enable benchmarking          |
| `log_enabled`       | bool | `True`  | Enable logging               |

### Logging Configuration

| Option           | Type | Default  | Description                                           |
| ---------------- | ---- | -------- | ----------------------------------------------------- |
| `log_level`      | str  | `"INFO"` | Minimum log level (DEBUG/INFO/WARNING/ERROR/CRITICAL) |
| `log_format`     | str  | `"rich"` | Output format (rich/plain/json)                       |
| `log_use_colors` | bool | `True`   | Use colored output                                    |
| `log_show_time`  | bool | `True`   | Show timestamps                                       |
| `log_show_level` | bool | `True`   | Show log levels                                       |
| `log_show_path`  | bool | `True`   | Show file paths                                       |

### Performance Settings

| Option                 | Type  | Default | Description                             |
| ---------------------- | ----- | ------- | --------------------------------------- |
| `trace_sampling_rate`  | float | `1.0`   | Fraction of traces to capture (0.0-1.0) |
| `trace_max_depth`      | int   | `50`    | Maximum trace depth                     |
| `profile_memory`       | bool  | `True`  | Track memory usage                      |
| `profile_min_duration` | float | `0.0`   | Minimum duration to profile (seconds)   |
| `benchmark_iterations` | int   | `100`   | Default benchmark iterations            |
| `benchmark_warmup`     | int   | `10`    | Warmup iterations                       |

### Analysis Settings

| Option                    | Type | Default | Description                                  |
| ------------------------- | ---- | ------- | -------------------------------------------- |
| `static_analysis_enabled` | bool | `True`  | Enable static code analysis                  |
| `auto_analyze`            | bool | `False` | Automatically analyze instrumented functions |
| `complexity_threshold`    | int  | `10`    | Complexity warning threshold                 |
| `type_checking_enabled`   | bool | `True`  | Enable type checking                         |
| `strict_thresholds`       | bool | `False` | Use strict quality thresholds                |

### Storage Settings

| Option                   | Type | Default                | Description                                    |
| ------------------------ | ---- | ---------------------- | ---------------------------------------------- |
| `storage_backend`        | str  | `"sqlite"`             | Storage backend (sqlite/postgresql/redis/none) |
| `storage_path`           | str  | `"~/.pydvlp/debug.db"` | Storage location                               |
| `storage_retention_days` | int  | `7`                    | Data retention period                          |
| `dashboard_enabled`      | bool | `False`                | Enable web dashboard                           |
| `dashboard_port`         | int  | `8888`                 | Dashboard port                                 |

## Advanced Configuration

### Dynamic Configuration

Change configuration at runtime based on conditions:

```python
from pydvlp.debug import debugkit
import os

# Configure based on user
if os.getenv("USER") == "developer":
    debugkit.configure(
        debug_enabled=True,
        profile_enabled=True,
        log_level="DEBUG"
    )

# Configure based on feature flags
if feature_flag("verbose_logging"):
    debugkit.configure(log_level="DEBUG")

# Configure based on performance
if system_load() > 0.8:
    debugkit.configure(
        profile_enabled=False,
        trace_enabled=False
    )
```

### Configuration Validation

```python
from pydvlp.debug.config import DevConfig

# Validate configuration
config = DevConfig()
try:
    config.validate()
    print("Configuration is valid")
except ValueError as e:
    print(f"Configuration error: {e}")

# Check specific settings
if config.is_production() and config.debug_enabled:
    print("Warning: Debug enabled in production!")
```

### Configuration Presets

Create reusable configuration presets:

```python
# config_presets.py
from pydvlp.debug.config import DevConfig, LogLevel, Environment

# Preset for API servers
API_SERVER_CONFIG = DevConfig(
    environment=Environment.PRODUCTION,
    log_enabled=True,
    log_format="json",
    log_level=LogLevel.INFO,
    profile_enabled=False,
    trace_enabled=False,
    storage_backend="redis"
)

# Preset for data processing
DATA_PROCESSING_CONFIG = DevConfig(
    environment=Environment.PRODUCTION,
    profile_enabled=True,
    profile_memory=True,
    benchmark_enabled=True,
    log_level=LogLevel.WARNING
)

# Preset for development
DEVELOPMENT_CONFIG = DevConfig(
    environment=Environment.DEVELOPMENT,
    debug_enabled=True,
    profile_enabled=True,
    trace_enabled=True,
    log_level=LogLevel.DEBUG,
    static_analysis_enabled=True,
    auto_analyze=True
)
```

### Per-Module Configuration

Configure different settings for different modules:

```python
# Configure for specific module
import logging

# Set module-specific log level
logging.getLogger("pydvlp.debug.analysis").setLevel(logging.WARNING)
logging.getLogger("pydvlp.debug.profiling").setLevel(logging.DEBUG)

# Or use custom configuration per context
with debugkit.context("critical_section") as ctx:
    # Temporarily enable profiling
    ctx.configure(profile_enabled=True)
    # ... critical code ...
```

## Configuration Best Practices

### 1. Use Environment Variables

Keep configuration in environment variables for flexibility:

```bash
# .env file
PYDVLP_ENVIRONMENT=${APP_ENV:-development}
PYDVLP_LOG_LEVEL=${LOG_LEVEL:-INFO}
PYDVLP_PROFILE_ENABLED=${ENABLE_PROFILING:-false}
```

### 2. Validate Early

Validate configuration at startup:

```python
# app.py
from pydvlp.debug import debugkit

def init_app():
    # Validate configuration
    try:
        debugkit.config.validate()
    except ValueError as e:
        print(f"Invalid configuration: {e}")
        sys.exit(1)

    # Log configuration
    debugkit.info("Application starting",
                  environment=debugkit.config.environment,
                  debug=debugkit.config.debug_enabled)
```

### 3. Document Configuration

Keep configuration documented:

```python
# config.py
"""Application configuration.

Environment Variables:
    PYDVLP_ENABLED: Enable PyDvlp Debug (default: true)
    PYDVLP_ENVIRONMENT: Environment name (default: development)
    PYDVLP_LOG_LEVEL: Logging level (default: INFO)
    ...
"""
```

### 4. Use Sensible Defaults

Provide good defaults that work for most cases:

```python
from pydvlp.debug import debugkit

# Only override what's necessary
debugkit.configure(
    log_level=os.getenv("LOG_LEVEL", "INFO"),
    profile_enabled=os.getenv("PROFILE", "false").lower() == "true"
)
```

### 5. Separate Concerns

Keep development and production configs separate:

```python
# config/development.py
DEBUG_CONFIG = {
    "debug_enabled": True,
    "profile_enabled": True,
    "log_level": "DEBUG",
    "auto_analyze": True
}

# config/production.py
PROD_CONFIG = {
    "debug_enabled": False,
    "profile_enabled": False,
    "log_level": "ERROR",
    "storage_backend": "none"
}

# Load appropriate config
if os.getenv("ENV") == "production":
    debugkit.configure(**PROD_CONFIG)
else:
    debugkit.configure(**DEBUG_CONFIG)
```

## Troubleshooting Configuration

### Configuration Not Taking Effect

```python
# Check current configuration
print(debugkit.config.to_dict())

# Verify environment variables
import os
print(f"PYDVLP_ENABLED: {os.getenv('PYDVLP_ENABLED')}")

# Force reload configuration
debugkit.config.reload()
```

### Performance Issues

If experiencing performance issues:

```python
# Disable expensive features
debugkit.configure(
    profile_enabled=False,
    trace_enabled=False,
    static_analysis_enabled=False,
    auto_analyze=False
)

# Or use production mode
os.environ["PYDVLP_ENVIRONMENT"] = "production"
```

### Debugging Configuration

```python
# Enable configuration debugging
debugkit.configure(config_debug=True)

# This will log all configuration changes
debugkit.configure(log_level="DEBUG")
# Logs: Configuration changed: log_level INFO -> DEBUG
```
