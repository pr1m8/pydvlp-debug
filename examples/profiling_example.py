#!/usr/bin/env python3
"""Performance profiling examples using PyDvlp Debug."""

from __future__ import annotations

import random

from pydvlp.debug import debugkit, profile_performance


def main():
    """Demonstrate profiling features."""
    print("=== Performance Profiling Examples ===\n")

    # Example 1: Basic function profiling
    print("1. Basic function profiling:")
    slow_calculation(1000)

    # Example 2: Comparing algorithms
    print("\n2. Comparing sorting algorithms:")
    data = [random.randint(1, 1000) for _ in range(1000)]

    bubble_sort(data.copy())
    quick_sort(data.copy())

    # Example 3: Memory profiling
    print("\n3. Memory-intensive operation:")
    memory_intensive_task()

    # Example 4: Context manager profiling
    print("\n4. Profiling with context manager:")
    with profile_performance() as prof:
        # Simulate complex operation
        result = 0
        for i in range(1000000):
            result += i**0.5
        print(f"Result: {result:.2f}")

    # Example 5: Comprehensive instrumentation
    print("\n5. Comprehensive instrumentation:")
    process_large_dataset(1000)


@profile_performance()
def slow_calculation(n: int) -> float:
    """Simulate a slow calculation."""
    debugkit.ice(n, "Starting calculation")
    result = 0.0

    for i in range(n):
        for j in range(n):
            result += (i * j) ** 0.5

    debugkit.ice(result, "Calculation complete")
    return result


@profile_performance(profiler="timeit")
def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@profile_performance(profiler="timeit")
def quick_sort(arr: list[int]) -> list[int]:
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


@profile_performance(profiler="memory_profiler")
def memory_intensive_task():
    """Demonstrate memory profiling."""
    # Create large data structures
    large_list = [i for i in range(1000000)]
    large_dict = {i: str(i) * 10 for i in range(100000)}

    # Process data
    filtered = [x for x in large_list if x % 2 == 0]
    result = sum(filtered)

    debugkit.ice(result, "Memory task result")
    return result


@debugkit.instrument(profile=True, trace=True, analyze=True)
def process_large_dataset(size: int) -> dict[str, any]:
    """Process a large dataset with full instrumentation."""
    # Generate data
    data = generate_dataset(size)

    # Process in batches
    batch_size = 100
    results = []

    for i in range(0, size, batch_size):
        batch = data[i : i + batch_size]
        processed = process_batch(batch)
        results.extend(processed)

    # Aggregate results
    summary = {
        "total_items": len(results),
        "average": sum(results) / len(results),
        "min": min(results),
        "max": max(results),
    }

    debugkit.ice(summary, "Dataset processing complete")
    return summary


def generate_dataset(size: int) -> list[float]:
    """Generate random dataset."""
    return [random.random() * 100 for _ in range(size)]


def process_batch(batch: list[float]) -> list[float]:
    """Process a batch of data."""
    # Simulate processing
    return [item**2 + item * 0.5 for item in batch]


if __name__ == "__main__":
    main()
