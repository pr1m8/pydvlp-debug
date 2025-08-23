#!/usr/bin/env python3
"""Performance profiling examples using PyDvlp Debug."""

from __future__ import annotations

import random
import time

from pydvlp.debug import debugkit, profile


def example_1_basic_profiling():
    """Basic function profiling."""
    print("\n=== Example 1: Basic Function Profiling ===")

    @profile.profile_performance
    def calculate_fibonacci(n):
        """Calculate fibonacci number recursively."""
        if n <= 1:
            return n
        return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

    # Profile the function
    result = calculate_fibonacci(10)
    print(f"Fibonacci(10) = {result}")

    # Profile with decorator options
    @profile.profile_performance
    def process_list(items):
        """Process a list of items."""
        time.sleep(0.1)  # Simulate work
        return [x * 2 for x in items]

    result = process_list([1, 2, 3, 4, 5])
    print(f"Processed list: {result}")


def example_2_memory_profiling():
    """Memory profiling examples."""
    print("\n=== Example 2: Memory Profiling ===")

    @profile.profile_memory
    def create_large_dataset(size):
        """Create a large dataset to observe memory usage."""
        data = []
        for i in range(size):
            data.append(
                {
                    "id": i,
                    "value": random.random(),
                    "text": f"Item {i}" * 10,
                }, )
        return data

    # Test with different sizes
    small_data = create_large_dataset(100)
    print(f"Created {len(small_data)} items")

    medium_data = create_large_dataset(1000)
    print(f"Created {len(medium_data)} items")


def example_3_context_profiling():
    """Using profiling context managers."""
    print("\n=== Example 3: Context-based Profiling ===")

    def complex_workflow():
        """A workflow with multiple steps to profile."""

        with profile.profiler("data_loading"):
            # Simulate data loading
            time.sleep(0.2)
            data = list(range(1000))

        with profile.profiler("data_processing"):
            # Process data
            time.sleep(0.3)
            processed = [x**2 for x in data]

        with profile.profiler("data_saving"):
            # Simulate saving
            time.sleep(0.1)
            result = sum(processed)

        return result

    result = complex_workflow()
    print(f"Workflow result: {result}")


def example_4_instrumented_profiling():
    """Using unified instrumentation with profiling."""
    print("\n=== Example 4: Instrumented Profiling ===")

    @debugkit.instrument(profile=True, log=True)
    def analyze_data(data):
        """Analyze data with full instrumentation."""
        # Step 1: Validate
        if not data:
            raise ValueError("Empty data")

        # Step 2: Process
        results = []
        for item in data:
            if item > 0:
                results.append(item**0.5)

        # Step 3: Aggregate
        return {
            "count": len(results),
            "sum": sum(results),
            "avg": sum(results) / len(results) if results else 0,
        }

    test_data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = analyze_data(test_data)
    print(f"Analysis result: {result}")


def example_5_comparative_profiling():
    """Compare performance of different implementations."""
    print("\n=== Example 5: Comparative Profiling ===")

    # Implementation 1: List comprehension
    @profile.profile_performance
    def filter_with_comprehension(data, threshold):
        return [x for x in data if x > threshold]

    # Implementation 2: Filter function
    @profile.profile_performance
    def filter_with_filter(data, threshold):
        return list(filter(lambda x: x > threshold, data))

    # Implementation 3: Generator
    @profile.profile_performance
    def filter_with_generator(data, threshold):
        return list(x for x in data if x > threshold)

    # Test data
    test_data = list(range(10000))
    threshold = 5000

    # Compare implementations
    result1 = filter_with_comprehension(test_data, threshold)
    filter_with_filter(test_data, threshold)
    filter_with_generator(test_data, threshold)

    print(f"All methods returned {len(result1)} items")


def example_6_nested_profiling():
    """Profiling nested function calls."""
    print("\n=== Example 6: Nested Function Profiling ===")

    @profile.profile_performance
    def outer_function(n):
        """Outer function that calls other functions."""
        data = prepare_data(n)
        processed = process_data(data)
        return finalize_results(processed)

    @profile.profile_performance
    def prepare_data(n):
        """Prepare initial data."""
        time.sleep(0.1)
        return list(range(n))

    @profile.profile_performance
    def process_data(data):
        """Process the data."""
        time.sleep(0.2)
        return [x * 2 for x in data]

    @profile.profile_performance
    def finalize_results(data):
        """Finalize and return results."""
        time.sleep(0.05)
        return sum(data)

    result = outer_function(100)
    print(f"Final result: {result}")

    # Get profiling statistics
    stats = profile.get_stats()
    print("\nProfiling Statistics:")
    for func_name, data in stats.items():
        if data["calls"] > 0:
            print(
                f"  {func_name}: {
                    data['calls']} calls, avg {
                    data['avg_time']:.3f}s", )


def example_7_conditional_profiling():
    """Conditional and sampled profiling."""
    print("\n=== Example 7: Conditional Profiling ===")

    # Profile only in development
    if debugkit.config.environment == "development":
        decorator = profile.profile_performance
    else:

        def decorator(f):
            return f  # No-op decorator

    @decorator
    def maybe_profiled_function():
        """Function that may or may not be profiled."""
        time.sleep(0.1)
        return "result"

    result = maybe_profiled_function()
    print(f"Result: {result}")

    # Sampling-based profiling
    def sampled_function():
        """Function to be profiled with sampling."""
        # Only profile 10% of calls
        if random.random() < 0.1:
            with profile.profiler("sampled_operation"):
                time.sleep(0.05)
                return "profiled"
        else:
            time.sleep(0.05)
            return "not profiled"

    # Call multiple times
    results = []
    for _ in range(20):
        results.append(sampled_function())

    profiled_count = results.count("profiled")
    print(f"Profiled {profiled_count}/20 calls")


def example_8_production_profiling():
    """Production-safe profiling patterns."""
    print("\n=== Example 8: Production Profiling ===")

    # Configure for production
    import os

    os.environ["PYDVLP_ENVIRONMENT"] = "production"
    os.environ["PYDVLP_PROFILE_ENABLED"] = "true"
    os.environ["PYDVLP_PROFILE_MIN_DURATION"] = "0.5"  # Only profile slow ops

    @profile.profile_performance
    def production_endpoint(request_data):
        """Simulated production endpoint."""
        # Fast operation - won't be profiled
        if request_data.get("fast"):
            time.sleep(0.1)
            return {"status": "fast"}

        # Slow operation - will be profiled
        if request_data.get("slow"):
            time.sleep(0.6)
            return {"status": "slow"}

        return {"status": "normal"}

    # Test different scenarios
    print("Testing fast request...")
    production_endpoint({"fast": True})

    print("Testing slow request...")
    production_endpoint({"slow": True})

    print("Testing normal request...")
    production_endpoint({})


def main():
    """Run all profiling examples."""
    print("PyDvlp Debug - Performance Profiling Examples")
    print("=" * 50)

    # Configure for examples
    debugkit.configure(
        profile_enabled=True,
        profile_memory=True,
        log_enabled=True,
    )

    # Run examples
    example_1_basic_profiling()
    example_2_memory_profiling()
    example_3_context_profiling()
    example_4_instrumented_profiling()
    example_5_comparative_profiling()
    example_6_nested_profiling()
    example_7_conditional_profiling()
    example_8_production_profiling()

    print("\n" + "=" * 50)
    print("Profiling examples complete!")

    # Show final statistics
    stats = profile.get_stats()
    if stats:
        print("\nOverall Statistics:")
        total_calls = sum(s["calls"] for s in stats.values())
        total_time = sum(s["total_time"] for s in stats.values())
        print(f"Total function calls profiled: {total_calls}")
        print(f"Total time in profiled functions: {total_time:.3f}s")


if __name__ == "__main__":
    main()
