#!/usr/bin/env python3
"""Benchmarking examples using PyDvlp Debug."""

from __future__ import annotations

import random
import time

from pydvlp.debug import benchmark, debugkit


def example_1_basic_benchmarking():
    """Basic benchmarking of functions."""
    print("\n=== Example 1: Basic Benchmarking ===")

    # Define functions to benchmark
    @benchmark.measure(iterations=1000)
    def bubble_sort(arr: list[int]) -> list[int]:
        """Bubble sort implementation."""
        n = len(arr)
        arr = arr.copy()  # Don't modify original
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @benchmark.measure(iterations=1000)
    def quick_sort(arr: list[int]) -> list[int]:
        """Quick sort implementation."""
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    @benchmark.measure(iterations=1000)
    def python_sort(arr: list[int]) -> list[int]:
        """Python's built-in sort."""
        return sorted(arr)

    # Test data
    test_data = [random.randint(1, 100) for _ in range(50)]

    # Run benchmarks
    print("Benchmarking sorting algorithms with 50 elements...")
    bubble_result = bubble_sort(test_data)
    quick_result = quick_sort(test_data)
    python_result = python_sort(test_data)

    # Verify all produce same result
    assert bubble_result == quick_result == python_result
    print("✅ All algorithms produce correct results")


def example_2_quick_comparison():
    """Quick comparison of different approaches."""
    print("\n=== Example 2: Quick Comparison ===")

    # Different ways to find maximum
    data = list(range(10000))
    random.shuffle(data)

    def max_loop(arr):
        """Find max using loop."""
        max_val = arr[0]
        for val in arr:
            if val > max_val:
                max_val = val
        return max_val

    def max_reduce(arr):
        """Find max using reduce."""
        from functools import reduce

        return reduce(lambda x, y: x if x > y else y, arr)

    def max_builtin(arr):
        """Find max using built-in."""
        return max(arr)

    # Quick benchmark
    print("Comparing max-finding approaches...")
    benchmark.quick_benchmark(
        lambda: max_loop(data),
        lambda: max_reduce(data),
        lambda: max_builtin(data),
        names=["Loop", "Reduce", "Built-in"],
        iterations=100,
    )


def example_3_context_benchmarking():
    """Benchmarking with context managers."""
    print("\n=== Example 3: Context-based Benchmarking ===")

    def process_data_pipeline(data):
        """Multi-step data processing pipeline."""

        with benchmark.timer("step1_validation"):
            # Validate data
            if not all(isinstance(x, (int, float)) for x in data):
                raise ValueError("Invalid data")
            time.sleep(0.01)  # Simulate work

        with benchmark.timer("step2_transformation"):
            # Transform data
            transformed = [x**2 for x in data]
            time.sleep(0.02)  # Simulate work

        with benchmark.timer("step3_filtering"):
            # Filter results
            filtered = [x for x in transformed if x > 100]
            time.sleep(0.01)  # Simulate work

        with benchmark.timer("step4_aggregation"):
            # Aggregate results
            result = {
                "sum": sum(filtered),
                "count": len(filtered),
                "avg": sum(filtered) / len(filtered) if filtered else 0,
            }
            time.sleep(0.005)  # Simulate work

        return result

    # Run pipeline
    test_data = list(range(100))
    process_data_pipeline(test_data)

    # Get timing breakdown
    timings = benchmark.get_timings()
    print("\nPipeline timing breakdown:")
    total_time = sum(timings.values())
    for step, duration in sorted(timings.items()):
        percentage = (duration / total_time) * 100
        print(f"  {step}: {duration:.3f}s ({percentage:.1f}%)")


def example_4_statistical_benchmarking():
    """Benchmarking with statistical analysis."""
    print("\n=== Example 4: Statistical Benchmarking ===")

    # Functions with variable performance
    def unstable_function():
        """Function with variable execution time."""
        sleep_time = random.uniform(0.001, 0.01)
        time.sleep(sleep_time)
        return sleep_time

    def stable_function():
        """Function with consistent execution time."""
        time.sleep(0.005)
        return 0.005

    # Benchmark with statistics
    print("Benchmarking function stability...")

    # Run multiple iterations
    unstable_times = []
    stable_times = []

    for _ in range(100):
        start = time.time()
        unstable_function()
        unstable_times.append(time.time() - start)

        start = time.time()
        stable_function()
        stable_times.append(time.time() - start)

    # Calculate statistics
    import statistics

    print("\nUnstable function:")
    print(f"  Mean: {statistics.mean(unstable_times):.6f}s")
    print(f"  Std Dev: {statistics.stdev(unstable_times):.6f}s")
    print(f"  Min: {min(unstable_times):.6f}s")
    print(f"  Max: {max(unstable_times):.6f}s")

    print("\nStable function:")
    print(f"  Mean: {statistics.mean(stable_times):.6f}s")
    print(f"  Std Dev: {statistics.stdev(stable_times):.6f}s")
    print(f"  Min: {min(stable_times):.6f}s")
    print(f"  Max: {max(stable_times):.6f}s")


def example_5_memory_benchmarking():
    """Benchmarking memory usage."""
    print("\n=== Example 5: Memory Benchmarking ===")

    @benchmark.measure_memory
    def create_list(size):
        """Create a list of given size."""
        return list(range(size))

    @benchmark.measure_memory
    def create_generator(size):
        """Create a generator of given size."""
        return (x for x in range(size))

    @benchmark.measure_memory
    def create_dict(size):
        """Create a dictionary of given size."""
        return {i: i**2 for i in range(size)}

    # Test different sizes
    sizes = [1000, 10000, 100000]

    print("Memory usage comparison:")
    for size in sizes:
        print(f"\nSize: {size:,}")
        create_list(size)
        create_generator(size)
        create_dict(size)


def example_6_real_world_benchmarking():
    """Real-world benchmarking scenario."""
    print("\n=== Example 6: Real-World Benchmarking ===")

    # Simulate different JSON parsing approaches
    import json

    # Create test data
    test_data = {
        "users": [
            {
                "id": i,
                "name": f"User{i}",
                "email": f"user{i}@example.com",
                "metadata": {
                    "created": "2024-01-01",
                    "preferences": {"theme": "dark", "lang": "en"},
                },
            }
            for i in range(1000)
        ],
    }
    json_str = json.dumps(test_data)

    @benchmark.measure(iterations=100)
    def parse_standard():
        """Standard JSON parsing."""
        return json.loads(json_str)

    @benchmark.measure(iterations=100)
    def parse_with_object_hook():
        """JSON parsing with object hook."""

        def object_hook(obj):
            # Convert to custom objects
            if "id" in obj and "name" in obj:
                return type("User", (), obj)
            return obj

        return json.loads(json_str, object_hook=object_hook)

    try:
        import ujson

        @benchmark.measure(iterations=100)
        def parse_ujson():
            """Ultra-fast JSON parsing."""
            return ujson.loads(json_str)

        has_ujson = True
    except ImportError:
        has_ujson = False

    # Run benchmarks
    print("Benchmarking JSON parsing methods...")
    parse_standard()
    parse_with_object_hook()
    if has_ujson:
        parse_ujson()

    # Compare results
    report = benchmark.get_report()
    print("\nBenchmark Report:")
    print(report.summary())


def example_7_automated_performance_testing():
    """Automated performance regression testing."""
    print("\n=== Example 7: Automated Performance Testing ===")

    class PerformanceTest:
        """Performance test helper."""

        def __init__(self, baseline=None):
            self.baseline = baseline or {}
            self.results = {}

        def test_function(self, func, name, threshold=1.2):
            """Test function performance against baseline."""
            # Measure current performance
            start = time.time()
            for _ in range(100):
                func()
            duration = time.time() - start
            avg_time = duration / 100

            self.results[name] = avg_time

            # Compare with baseline
            if name in self.baseline:
                baseline_time = self.baseline[name]
                ratio = avg_time / baseline_time

                if ratio > threshold:
                    print(
                        f"❌ {name}: Performance regression! "
                        f"{ratio:.2f}x slower than baseline",
                    )
                    return False
                else:
                    print(f"✅ {name}: Performance OK ({ratio:.2f}x vs baseline)")
                    return True
            else:
                print(f"📊 {name}: New baseline {avg_time:.6f}s")
                return True

    # Define baseline performance
    baseline = {
        "string_concat": 0.001,
        "list_append": 0.0008,
        "dict_update": 0.0012,
    }

    # Create test
    perf_test = PerformanceTest(baseline)

    # Test functions
    def test_string_concat():
        result = ""
        for i in range(100):
            result += str(i)
        return result

    def test_list_append():
        result = []
        for i in range(100):
            result.append(i)
        return result

    def test_dict_update():
        result = {}
        for i in range(100):
            result[i] = i**2
        return result

    # Run tests
    print("Running performance tests...")
    all_passed = True
    all_passed &= perf_test.test_function(test_string_concat, "string_concat")
    all_passed &= perf_test.test_function(test_list_append, "list_append")
    all_passed &= perf_test.test_function(test_dict_update, "dict_update")

    if all_passed:
        print("\n✅ All performance tests passed!")
    else:
        print("\n❌ Performance regressions detected!")

    # Save new baseline
    print("\nNew baseline values:")
    for name, time in perf_test.results.items():
        print(f"  {name}: {time:.6f}s")


def example_8_comparative_benchmarking():
    """Compare different implementations."""
    print("\n=== Example 8: Comparative Benchmarking ===")

    # Different string formatting methods
    name = "Alice"
    age = 30
    city = "New York"

    @benchmark.measure(iterations=10000)
    def format_concatenation():
        return "Name: " + name + ", Age: " + str(age) + ", City: " + city

    @benchmark.measure(iterations=10000)
    def format_percent():
        return "Name: %s, Age: %d, City: %s" % (name, age, city)

    @benchmark.measure(iterations=10000)
    def format_method():
        return f"Name: {name}, Age: {age}, City: {city}"

    @benchmark.measure(iterations=10000)
    def format_fstring():
        return f"Name: {name}, Age: {age}, City: {city}"

    # Run all formatting methods
    print("Benchmarking string formatting methods...")
    concat_result = format_concatenation()
    percent_result = format_percent()
    method_result = format_method()
    fstring_result = format_fstring()

    # Verify all produce same result
    assert concat_result == percent_result == method_result == fstring_result

    # Get detailed comparison
    stats = benchmark.get_stats()

    # Find fastest method
    fastest = min(stats.items(), key=lambda x: x[1]["avg_time"])
    print(f"\n🏆 Fastest method: {fastest[0].replace('format_', '')}")

    # Show relative performance
    fastest_time = fastest[1]["avg_time"]
    print("\nRelative performance:")
    for name, data in sorted(stats.items()):
        relative = data["avg_time"] / fastest_time
        print(f"  {name.replace('format_', '')}: {relative:.2f}x")


def main():
    """Run all benchmarking examples."""
    print("PyDvlp Debug - Benchmarking Examples")
    print("=" * 50)

    # Configure for benchmarking
    debugkit.configure(
        benchmark_enabled=True,
        profile_enabled=False,  # Disable profiling for cleaner output
        log_enabled=False,
    )

    # Run examples
    example_1_basic_benchmarking()
    example_2_quick_comparison()
    example_3_context_benchmarking()
    example_4_statistical_benchmarking()
    example_5_memory_benchmarking()
    example_6_real_world_benchmarking()
    example_7_automated_performance_testing()
    example_8_comparative_benchmarking()

    print("\n" + "=" * 50)
    print("Benchmarking examples complete!")

    # Final summary
    print("\nOverall Benchmark Summary:")
    final_report = benchmark.get_report()
    if final_report:
        print(final_report.summary())


if __name__ == "__main__":
    main()
