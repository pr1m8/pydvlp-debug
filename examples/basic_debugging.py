#!/usr/bin/env python3
"""Basic debugging examples using PyDvlp Debug."""

from __future__ import annotations

from pydvlp.debug import debug, debugkit


def main():
    """Demonstrate basic debugging features."""
    print("=== Basic Debugging Examples ===\n")

    # Configure for examples
    debugkit.configure(
        debug_enabled=True,
        log_enabled=True,
        log_level="INFO",
    )

    # Example 1: Simple variable debugging
    print("1. Simple variable debugging:")
    x = 42
    y = "hello"
    debug.ice(x)  # Output: 🔍 42
    debug.ice(x, y)  # Output: 🔍 42 | 'hello'

    # Example 2: Debugging with labels
    print("\n2. Debugging with labels:")
    result = calculate_sum(10, 20)
    debug.ice("Sum result", result)

    # Example 3: Debugging complex objects
    print("\n3. Debugging complex objects:")
    data = {
        "users": ["alice", "bob", "charlie"],
        "scores": [95, 87, 92],
        "metadata": {
            "version": "1.0",
            "timestamp": "2024-01-01",
        },
    }
    debug.ice("User data", data)

    # Example 4: Debugging in loops
    print("\n4. Debugging in loops:")
    for i in range(3):
        value = i**2
        debug.ice(f"Iteration {i}", i=i, value=value)

    # Example 5: Conditional debugging
    print("\n5. Conditional debugging:")
    scores = [75, 92, 68, 88, 95]
    for score in scores:
        if score > 90:
            debug.ice("High score!", score)

    # Example 6: Function return debugging
    print("\n6. Function return debugging:")
    result = process_data([1, 2, 3, 4, 5])
    debug.ice("Processed data", result)


def calculate_sum(a: int, b: int) -> int:
    """Calculate sum with debugging."""
    debug.ice("Input values", a=a, b=b)
    result = a + b
    debug.ice("Calculated sum", result)
    return result


def process_data(items: list[int]) -> dict[str, any]:
    """Process data with debugging at each step."""
    debug.ice("Original items", items)

    # Step 1: Filter
    filtered = [x for x in items if x > 2]
    debug.ice("After filtering", filtered)

    # Step 2: Transform
    transformed = [x * 2 for x in filtered]
    debug.ice("After transformation", transformed)

    # Step 3: Aggregate
    result = {
        "count": len(transformed),
        "sum": sum(transformed),
        "average": sum(transformed) / len(transformed) if transformed else 0,
        "items": transformed,
    }
    debug.ice("Final result", result)

    return result


if __name__ == "__main__":
    main()
