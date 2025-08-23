# Best Practices Guide

This guide covers best practices for using PyDvlp Debug effectively in your Python projects.

## General Principles

### 1. Start Simple, Add Complexity Gradually

Begin with basic debugging and add features as needed:

```python
# Start with simple debugging
from pydvlp.debug import debug
debug.ice(variable)

# Add profiling when needed
from pydvlp.debug import profile
@profile.profile_performance
def slow_function():
    pass

# Add full instrumentation for complex cases
from pydvlp.debug import debugkit
@debugkit.instrument(analyze=True, profile=True)
def critical_function():
    pass
```

### 2. Use Appropriate Tools for the Task

Choose the right tool for your debugging needs:

- **`debug.ice()`** - Quick variable inspection
- **`debugkit.context()`** - Grouped operations with timing
- **`profile.profile_performance`** - Performance bottlenecks
- **`benchmark.measure()`** - Comparing implementations
- **`debugkit.analyze_code()`** - Code quality assessment

### 3. Configure for Your Environment

Always configure appropriately for your environment:

```python
import os
from pydvlp.debug import debugkit

# Automatic environment detection
env = os.getenv("APP_ENV", "development")
os.environ["PYDVLP_ENVIRONMENT"] = env

# Environment-specific configuration
if env == "production":
    debugkit.configure(
        log_level="ERROR",
        debug_enabled=False,
        profile_enabled=False
    )
elif env == "development":
    debugkit.configure(
        log_level="DEBUG",
        debug_enabled=True,
        profile_enabled=True
    )
```

## Debugging Best Practices

### 1. Use Meaningful Labels

Add context to your debug output:

```python
# Bad
debug.ice(x, y, z)

# Good
debug.ice("User validation", user_id=x, status=y, attempts=z)

# Better
debug.ice(f"User {user_id} validation",
          status=status,
          attempts=attempts,
          elapsed=time.time() - start)
```

### 2. Debug at Key Points

Focus debugging on important state changes:

```python
def process_order(order):
    debug.ice("Order received", order_id=order.id, total=order.total)

    # Validate
    if not validate_order(order):
        debug.ice("Order validation failed",
                  order_id=order.id,
                  errors=order.errors)
        return None

    # Process payment
    payment_result = process_payment(order)
    debug.ice("Payment processed",
              order_id=order.id,
              success=payment_result.success)

    # Ship order
    if payment_result.success:
        shipping = ship_order(order)
        debug.ice("Order shipped",
                  order_id=order.id,
                  tracking=shipping.tracking_number)

    return order
```

### 3. Use Conditional Debugging

Debug only when necessary:

```python
# Debug only errors
if result.error:
    debug.ice("Operation failed", error=result.error, context=context)

# Debug based on verbosity
if debugkit.config.debug_enabled and verbose:
    debug.ice("Detailed info", data=large_data_structure)

# Debug sampling
if random.random() < 0.01:  # 1% of requests
    debug.ice("Sampled request", request=request.to_dict())
```

## Profiling Best Practices

### 1. Profile Hot Paths

Focus profiling on frequently called or slow operations:

```python
# Profile critical paths
@profile.profile_performance
def api_endpoint(request):
    # This is called thousands of times
    return process_request(request)

# Don't profile everything
def utility_function(x):
    # Simple, fast function - no need to profile
    return x * 2
```

### 2. Use Context Managers for Granular Profiling

Profile specific sections:

```python
def complex_workflow(data):
    with profile.profiler("data_validation"):
        validate_data(data)

    with profile.profiler("data_transformation"):
        transformed = transform_data(data)

    with profile.profiler("data_persistence"):
        save_data(transformed)

    # Get breakdown of where time was spent
    stats = profile.get_stats()
    log_performance_metrics(stats)
```

### 3. Set Meaningful Thresholds

Only profile operations that matter:

```python
# Configure minimum duration
profile_settings = {
    "min_duration": 0.1  # Only profile ops > 100ms
}

@profile.profile_performance(**profile_settings)
def potentially_slow_operation():
    pass
```

## Logging Best Practices

### 1. Use Appropriate Log Levels

Choose the right level for your messages:

```python
# DEBUG - Detailed information for diagnosing problems
debugkit.config.debug_enabled and debug.ice("Detailed state", state=obj)

# INFO - General informational messages
debugkit.info("Server started", port=8080, workers=4)

# SUCCESS - Successful completion of operations
debugkit.success("Deployment complete", version="1.2.0")

# WARNING - Warning messages
log.warning("High memory usage", usage_mb=1024, threshold_mb=800)

# ERROR - Error messages that don't stop execution
debugkit.error("Failed to send email", user_id=user.id, retry=True)

# CRITICAL - Critical errors that may stop execution
log.critical("Database connection lost", error=str(e))
```

### 2. Structure Your Logs

Use structured logging for better analysis:

```python
# Include relevant context
debugkit.info("Order processed",
    order_id=order.id,
    user_id=order.user_id,
    total=order.total,
    items_count=len(order.items),
    processing_time=elapsed_time,
    payment_method=order.payment_method
)

# Use consistent field names
# Always use 'user_id', not sometimes 'user' or 'uid'
# Always use 'duration_ms', not sometimes 'time' or 'elapsed'
```

### 3. Avoid Logging Sensitive Data

Never log passwords, tokens, or PII:

```python
# Bad
debugkit.info("User login", username=username, password=password)

# Good
debugkit.info("User login",
    username=username,
    ip_address=request.ip,
    user_agent=request.user_agent
)

# Sanitize sensitive data
def sanitize_user(user):
    return {
        "id": user.id,
        "username": user.username,
        "email": f"{user.email[:3]}***@{user.email.split('@')[1]}"
    }

debugkit.info("User created", user=sanitize_user(new_user))
```

## Context Management Best Practices

### 1. Use Contexts for Related Operations

Group related operations together:

```python
with debugkit.context("user_session", user_id=user.id) as ctx:
    # All operations in this context are associated
    ctx.debug("Session started")

    # Load user data
    user_data = load_user_data(user.id)
    ctx.checkpoint("data_loaded")

    # Process request
    result = process_user_request(user_data, request)
    ctx.checkpoint("request_processed")

    # Save results
    save_results(result)
    ctx.checkpoint("results_saved")

    ctx.success("Session completed", duration=ctx.elapsed)
```

### 2. Use Meaningful Context Names

Choose descriptive context names:

```python
# Good context names
with debugkit.context("payment_processing"):
    pass

with debugkit.context("email_delivery"):
    pass

with debugkit.context("data_import"):
    pass

# Bad context names
with debugkit.context("process"):
    pass

with debugkit.context("task"):
    pass
```

### 3. Track Important Checkpoints

Use checkpoints to track progress:

```python
with debugkit.context("batch_processing") as ctx:
    for i, batch in enumerate(batches):
        ctx.checkpoint(f"batch_{i}_start")

        try:
            process_batch(batch)
            ctx.checkpoint(f"batch_{i}_complete")
        except Exception as e:
            ctx.error(f"Batch {i} failed", error=str(e))
            ctx.checkpoint(f"batch_{i}_failed")
```

## Code Analysis Best Practices

### 1. Regular Code Quality Checks

Integrate code analysis into your workflow:

```python
# pre-commit hook
def pre_commit_check():
    """Check code quality before commit."""
    files_to_check = get_changed_python_files()

    failed = False
    for file_path in files_to_check:
        functions = extract_functions(file_path)
        for func in functions:
            report = debugkit.analyze_code(func)

            if report.combined_score < 70:
                print(f"❌ {func.__name__}: Low quality ({report.combined_score}/100)")
                failed = True

            if report.complexity_analysis.risk_score > 50:
                print(f"⚠️  {func.__name__}: High complexity")
                failed = True

    return 0 if not failed else 1
```

### 2. Set Quality Standards

Define and enforce quality standards:

```python
# quality_standards.py
QUALITY_THRESHOLDS = {
    "min_quality_score": 70,
    "max_complexity": 15,
    "min_type_coverage": 0.8,
    "max_function_length": 50
}

def check_function_quality(func):
    """Check if function meets quality standards."""
    report = debugkit.analyze_code(func)

    issues = []

    if report.combined_score < QUALITY_THRESHOLDS["min_quality_score"]:
        issues.append(f"Low quality score: {report.combined_score}")

    if report.complexity_analysis.cyclomatic_complexity > QUALITY_THRESHOLDS["max_complexity"]:
        issues.append(f"High complexity: {report.complexity_analysis.cyclomatic_complexity}")

    if report.type_analysis.type_coverage < QUALITY_THRESHOLDS["min_type_coverage"]:
        issues.append(f"Low type coverage: {report.type_analysis.type_coverage:.1%}")

    return issues
```

### 3. Act on Recommendations

Use analysis recommendations to improve code:

```python
def improve_function(func):
    """Analyze and improve function based on recommendations."""
    report = debugkit.analyze_code(func)

    print(f"Analyzing {func.__name__}...")
    print(f"Current score: {report.combined_score}/100")

    if report.recommendations:
        print("\nRecommendations:")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"{i}. {rec}")

        # Automated improvements
        if "Add type hints" in report.recommendations[0]:
            print("\n→ Adding type hints...")
            # Use automated tool to add type hints

        if "Reduce complexity" in report.recommendations[0]:
            print("\n→ Suggesting function decomposition...")
            # Suggest how to break down the function
```

## Performance Best Practices

### 1. Benchmark Before Optimizing

Always measure before optimizing:

```python
from pydvlp.debug import benchmark

# Benchmark current implementation
@benchmark.measure(iterations=1000)
def current_algorithm(data):
    return process_data_v1(data)

# Benchmark proposed optimization
@benchmark.measure(iterations=1000)
def optimized_algorithm(data):
    return process_data_v2(data)

# Compare results
results = benchmark.compare(
    current_algorithm,
    optimized_algorithm,
    test_data=sample_data
)

if results['optimized_algorithm']['avg_time'] < results['current_algorithm']['avg_time']:
    print("✅ Optimization successful!")
else:
    print("❌ Optimization made things worse!")
```

### 2. Profile in Production (Carefully)

Use sampling for production profiling:

```python
# Production profiling with sampling
def production_endpoint(request):
    # Only profile 0.1% of requests
    should_profile = random.random() < 0.001

    if should_profile:
        with profile.profiler("endpoint_processing"):
            result = process_request(request)

            # Log profiling results asynchronously
            async_log_profile_data(profile.get_last_profile())
    else:
        result = process_request(request)

    return result
```

### 3. Clear Profiling Data

Clean up profiling data regularly:

```python
# Clear profiling data between test runs
def run_performance_tests():
    profile.clear_stats()

    # Run tests
    test_suite_1()
    stats_1 = profile.get_stats()

    profile.clear_stats()

    test_suite_2()
    stats_2 = profile.get_stats()

    compare_performance(stats_1, stats_2)
```

## Integration Best Practices

### 1. CI/CD Integration

Add PyDvlp Debug to your CI/CD pipeline:

```yaml
# .github/workflows/quality.yml
- name: Code Quality Check
  run: |
    python -m pydvlp.debug.analyze --min-score 70 --max-complexity 15

- name: Performance Regression Check
  run: |
    python -m pydvlp.debug.benchmark --compare baseline.json
```

### 2. Monitoring Integration

Send metrics to monitoring systems:

```python
from pydvlp.debug import debugkit
import statsd

statsd_client = statsd.StatsClient('localhost', 8125)

# Send profiling metrics
@debugkit.instrument(profile=True)
def monitored_function():
    result = do_work()

    # Send metrics
    if hasattr(monitored_function, '_last_profile'):
        profile_data = monitored_function._last_profile
        statsd_client.timing('function.duration', profile_data['duration'] * 1000)
        statsd_client.gauge('function.memory', profile_data['memory_delta'])

    return result
```

### 3. Testing Integration

Use PyDvlp Debug in tests:

```python
import pytest
from pydvlp.debug import debugkit

@pytest.fixture
def enable_debug():
    """Enable debugging for tests."""
    original = debugkit.config.debug_enabled
    debugkit.configure(debug_enabled=True)
    yield
    debugkit.configure(debug_enabled=original)

def test_complex_algorithm(enable_debug):
    """Test with debugging enabled."""
    # Debug output will be visible during test failures
    result = complex_algorithm(test_data)
    assert result == expected
```

## Common Pitfalls to Avoid

### 1. Over-instrumentation

Don't instrument everything:

```python
# Bad - Too much instrumentation
@debugkit.instrument(analyze=True, profile=True, trace=True)
def add(a, b):
    return a + b

# Good - Instrument only what matters
@debugkit.instrument(profile=True)
def process_large_dataset(data):
    # Complex processing
    pass
```

### 2. Leaving Debug Code in Production

Always check environment:

```python
# Bad
debug.ice("Sensitive data", password=user.password)

# Good
if debugkit.config.environment == "development":
    debug.ice("User data", user_id=user.id)
```

### 3. Ignoring Performance Impact

Be aware of performance overhead:

```python
# Bad - Analyzing in a tight loop
for item in million_items:
    report = debugkit.analyze_code(process_item)  # Very expensive!

# Good - Analyze once or sample
if should_analyze:
    report = debugkit.analyze_code(process_item)
```

## Summary

1. **Start simple** and add complexity as needed
2. **Configure appropriately** for each environment
3. **Use meaningful names** and labels
4. **Focus on what matters** - don't over-instrument
5. **Measure before optimizing**
6. **Integrate into your workflow** - CI/CD, monitoring, testing
7. **Be mindful of performance** overhead
8. **Never log sensitive data**
9. **Use structured logging** for better analysis
10. **Act on analysis recommendations** to improve code quality
