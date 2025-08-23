#!/usr/bin/env python3
"""Production configuration examples for PyDvlp Debug."""

from __future__ import annotations

import os
import random
import time
from typing import Any

from pydvlp.debug import debugkit


def example_1_production_setup():
    """Example of production-safe configuration."""
    print("\n=== Example 1: Production Configuration ===")

    # Set production environment
    os.environ["PYDVLP_ENVIRONMENT"] = "production"
    os.environ["PYDVLP_DEBUG_ENABLED"] = "false"
    os.environ["PYDVLP_PROFILE_ENABLED"] = "false"
    os.environ["PYDVLP_LOG_LEVEL"] = "ERROR"
    os.environ["PYDVLP_LOG_FORMAT"] = "json"

    # Reload configuration
    debugkit.configure()

    print(f"Environment: {debugkit.config.environment}")
    print(f"Debug enabled: {debugkit.config.debug_enabled}")
    print(f"Profile enabled: {debugkit.config.profile_enabled}")
    print(f"Log level: {debugkit.config.log_level}")

    # These will not produce output in production
    debugkit.ice("This won't show")
    debugkit.info("This won't show")

    # Only errors are logged
    debugkit.error("Critical error", error_code="E001")


def example_2_conditional_instrumentation():
    """Conditional instrumentation based on environment."""
    print("\n=== Example 2: Conditional Instrumentation ===")

    # Different configurations for different environments
    def get_instrumentation_config():
        """Get instrumentation config based on environment."""
        env = os.getenv("APP_ENV", "development")

        if env == "production":
            return {
                "profile": False,
                "debug": False,
                "analyze": False,
                "log": True,
            }
        elif env == "staging":
            return {
                "profile": True,  # Profile in staging
                "debug": False,
                "analyze": False,
                "log": True,
            }
        else:  # development
            return {
                "profile": True,
                "debug": True,
                "analyze": True,
                "log": True,
            }

    config = get_instrumentation_config()

    @debugkit.instrument(**config)
    def api_endpoint(request_data: dict[str, Any]) -> dict[str, Any]:
        """API endpoint with environment-aware instrumentation."""
        # Process request
        if not request_data:
            raise ValueError("Empty request data")

        # Simulate processing
        time.sleep(0.01)

        return {
            "status": "success",
            "data": {"processed": len(request_data)},
            "timestamp": time.time(),
        }

    # Test the endpoint
    test_request = {"user_id": 123, "action": "get_data"}
    try:
        result = api_endpoint(test_request)
        print(f"API result: {result['status']}")
    except Exception as e:
        debugkit.error("API error", error=str(e))


def example_3_sampling_based_profiling():
    """Sampling-based profiling for production."""
    print("\n=== Example 3: Sampling-based Profiling ===")

    # Configure sampling rate
    os.environ["PYDVLP_PROFILE_SAMPLE_RATE"] = "0.01"  # 1% of requests

    class ProductionProfiler:
        """Production-safe profiler with sampling."""

        def __init__(self, sample_rate: float = 0.01):
            self.sample_rate = sample_rate
            self.profile_count = 0
            self.total_requests = 0

        def maybe_profile(self, func_name: str):
            """Maybe profile based on sampling rate."""
            self.total_requests += 1

            if random.random() < self.sample_rate:
                self.profile_count += 1
                return debugkit.context(f"profile_{func_name}")
            else:
                # Return no-op context manager
                from contextlib import nullcontext

                return nullcontext()

        def get_stats(self):
            """Get profiling statistics."""
            return {
                "total_requests": self.total_requests,
                "profiled_requests": self.profile_count,
                "sample_rate": (
                    self.profile_count / self.total_requests
                    if self.total_requests > 0
                    else 0
                ),
            }

    profiler = ProductionProfiler(sample_rate=0.1)  # 10% for demo

    def production_function(data: list[int]) -> dict[str, Any]:
        """Function with production profiling."""
        with profiler.maybe_profile("production_function"):
            # Simulate work
            time.sleep(0.001)
            result = sum(data)

            # Log only important events
            if result > 1000:
                debugkit.error("High result detected", result=result)

            return {"sum": result, "count": len(data)}

    # Run multiple requests to see sampling
    print("Running sampled profiling...")
    for i in range(100):
        test_data = [random.randint(1, 10) for _ in range(random.randint(5, 15))]
        production_function(test_data)

    stats = profiler.get_stats()
    print(f"Profiling stats: {stats}")


def example_4_error_only_logging():
    """Error-only logging for production."""
    print("\n=== Example 4: Error-only Logging ===")

    # Configure for error-only logging
    debugkit.configure(
        log_level="ERROR",
        debug_enabled=False,
        profile_enabled=False,
    )

    def process_batch(items: list[dict[str, Any]]) -> dict[str, Any]:
        """Process batch with error-only logging."""
        processed = []
        errors = []

        for i, item in enumerate(items):
            try:
                # Simulate processing
                if not isinstance(item, dict):
                    raise TypeError(f"Item {i} is not a dictionary")

                if "id" not in item:
                    raise KeyError(f"Item {i} missing 'id' field")

                # These won't show up in production (not ERROR level)
                debugkit.info(f"Processing item {i}")  # Won't show
                debugkit.debug(f"Item details: {item}")  # Won't show

                # Process item
                processed_item = {
                    "id": item["id"],
                    "processed": True,
                    "timestamp": time.time(),
                }
                processed.append(processed_item)

            except Exception as e:
                # This will show up (ERROR level)
                debugkit.error(
                    f"Failed to process item {i}",
                    error=str(e),
                    item=item,
                )
                errors.append({"index": i, "error": str(e)})

        # Log final error summary if any errors
        if errors:
            debugkit.error(
                "Batch processing completed with errors",
                total_items=len(items),
                processed=len(processed),
                errors=len(errors),
            )

        return {
            "processed": processed,
            "errors": errors,
            "summary": {
                "total": len(items),
                "success": len(processed),
                "failed": len(errors),
            },
        }

    # Test with mixed data (some will fail)
    test_data = [
        {"id": 1, "value": "a"},
        {"id": 2, "value": "b"},
        "invalid_item",  # Will cause error
        {"value": "no_id"},  # Will cause error
        {"id": 3, "value": "c"},
    ]

    result = process_batch(test_data)
    print(f"Batch result: {result['summary']}")


def example_5_feature_flags_integration():
    """Integration with feature flags for production control."""
    print("\n=== Example 5: Feature Flags Integration ===")

    # Simulate feature flag system
    class FeatureFlags:
        """Simple feature flag system."""

        def __init__(self):
            self._flags = {
                "debug_logging": False,
                "performance_profiling": False,
                "detailed_tracing": False,
                "code_analysis": False,
            }

        def is_enabled(self, flag: str) -> bool:
            """Check if feature flag is enabled."""
            return self._flags.get(flag, False)

        def enable(self, flag: str):
            """Enable a feature flag."""
            self._flags[flag] = True

        def disable(self, flag: str):
            """Disable a feature flag."""
            self._flags[flag] = False

    # Create feature flags instance
    flags = FeatureFlags()

    # Enable some flags for demonstration
    flags.enable("performance_profiling")

    def configure_with_flags():
        """Configure debugging based on feature flags."""
        debugkit.configure(
            debug_enabled=flags.is_enabled("debug_logging"),
            profile_enabled=flags.is_enabled("performance_profiling"),
            trace_enabled=flags.is_enabled("detailed_tracing"),
            static_analysis_enabled=flags.is_enabled("code_analysis"),
        )

    # Apply configuration
    configure_with_flags()

    @debugkit.instrument(
        profile=debugkit.config.profile_enabled,
        analyze=debugkit.config.static_analysis_enabled,
    )
    def feature_controlled_function(data: list[str]) -> str:
        """Function controlled by feature flags."""
        if debugkit.config.debug_enabled:
            debugkit.ice("Debug info", data_size=len(data))

        # Process data
        result = " ".join(data)

        if debugkit.config.trace_enabled:
            debugkit.info("Tracing enabled", result_length=len(result))

        return result

    # Test function
    test_data = ["hello", "world", "from", "production"]
    result = feature_controlled_function(test_data)
    print(f"Result: {result}")

    # Show current configuration
    print(
        f"Current config: debug={debugkit.config.debug_enabled}, "
        f"profile={debugkit.config.profile_enabled}",
    )


def example_6_monitoring_integration():
    """Integration with monitoring systems."""
    print("\n=== Example 6: Monitoring Integration ===")

    class MockMetrics:
        """Mock metrics client for demonstration."""

        def __init__(self):
            self.metrics = {}

        def increment(self, metric: str, tags: dict[str, str] = None):
            """Increment a counter metric."""
            key = f"{metric}_{tags}" if tags else metric
            self.metrics[key] = self.metrics.get(key, 0) + 1

        def timing(self, metric: str, duration: float, tags: dict[str, str] = None):
            """Record timing metric."""
            key = f"{metric}_timing_{tags}" if tags else f"{metric}_timing"
            if key not in self.metrics:
                self.metrics[key] = []
            self.metrics[key].append(duration)

        def gauge(self, metric: str, value: float, tags: dict[str, str] = None):
            """Record gauge metric."""
            key = f"{metric}_gauge_{tags}" if tags else f"{metric}_gauge"
            self.metrics[key] = value

        def get_metrics(self):
            """Get all recorded metrics."""
            return self.metrics

    # Create metrics client
    metrics = MockMetrics()

    def monitored_function(operation_type: str, data: list[int]) -> dict[str, Any]:
        """Function with monitoring integration."""
        start_time = time.time()

        # Increment operation counter
        metrics.increment("operations.started", {"type": operation_type})

        try:
            with debugkit.context(f"operation_{operation_type}") as ctx:
                # Process data
                if operation_type == "sum":
                    result = sum(data)
                elif operation_type == "average":
                    result = sum(data) / len(data) if data else 0
                elif operation_type == "max":
                    result = max(data) if data else 0
                else:
                    raise ValueError(f"Unknown operation: {operation_type}")

                # Record processing time
                duration = time.time() - start_time
                metrics.timing(
                    "operations.duration",
                    duration,
                    {"type": operation_type},
                )

                # Record data size
                metrics.gauge(
                    "operations.data_size",
                    len(data),
                    {"type": operation_type},
                )

                # Success
                metrics.increment("operations.success", {"type": operation_type})

                ctx.success(
                    f"Operation {operation_type} completed",
                    result=result,
                    duration=duration,
                )

                return {"result": result, "duration": duration}

        except Exception as e:
            # Record error
            metrics.increment("operations.error", {"type": operation_type})

            debugkit.error(
                f"Operation {operation_type} failed",
                error=str(e),
                duration=time.time() - start_time,
            )
            raise

    # Test monitoring
    operations = [
        ("sum", [1, 2, 3, 4, 5]),
        ("average", [10, 20, 30]),
        ("max", [100, 200, 150]),
        ("invalid", [1, 2, 3]),  # This will fail
    ]

    for op_type, test_data in operations:
        try:
            result = monitored_function(op_type, test_data)
            print(f"{op_type}: {result['result']}")
        except Exception:
            print(f"{op_type}: failed")

    # Show collected metrics
    print(f"\nCollected metrics: {metrics.get_metrics()}")


def main():
    """Run all production configuration examples."""
    print("PyDvlp Debug - Production Configuration Examples")
    print("=" * 60)

    # Save original environment
    original_env = os.environ.copy()

    try:
        # Run examples
        example_1_production_setup()
        example_2_conditional_instrumentation()
        example_3_sampling_based_profiling()
        example_4_error_only_logging()
        example_5_feature_flags_integration()
        example_6_monitoring_integration()

        print("\n" + "=" * 60)
        print("Production configuration examples complete!")

        # Show final configuration
        print("\nFinal Configuration:")
        print(f"  Environment: {debugkit.config.environment}")
        print(f"  Debug: {debugkit.config.debug_enabled}")
        print(f"  Profile: {debugkit.config.profile_enabled}")
        print(f"  Log Level: {debugkit.config.log_level}")

    finally:
        # Restore original environment
        os.environ.clear()
        os.environ.update(original_env)


if __name__ == "__main__":
    main()
