#!/usr/bin/env python3
"""Code analysis examples using PyDvlp Debug."""

from __future__ import annotations

from pathlib import Path

from pydvlp.debug import debugkit


def main():
    """Demonstrate code analysis features."""
    print("=== Code Analysis Examples ===\n")

    # Example 1: Analyze a simple function
    print("1. Analyzing a simple function:")
    report = debugkit.analyze_code(simple_function)
    report.display()

    # Example 2: Analyze a complex function
    print("\n2. Analyzing a complex function:")
    report = debugkit.analyze_code(complex_function)
    print(f"Complexity score: {report.complexity_score}")
    print(f"Type coverage: {report.type_coverage:.1%}")
    print(f"Issues found: {len(report.issues)}")
    for issue in report.issues:
        print(f"  - {issue}")

    # Example 3: Analyze a class
    print("\n3. Analyzing a class:")
    report = debugkit.analyze_code(DataProcessor)
    report.display()

    # Example 4: Analyze this file
    print("\n4. Analyzing this file:")
    this_file = Path(__file__)
    report = debugkit.analyze_code(this_file)
    print(f"File: {this_file.name}")
    print(f"Overall complexity: {report.complexity_score}")
    print("Suggestions:")
    for suggestion in report.suggestions:
        print(f"  - {suggestion}")


def simple_function(x: int, y: int) -> int:
    """A simple function with good practices."""
    return x + y


def complex_function(data: list, threshold=None, verbose=False):
    """A complex function with various issues."""
    result = []

    # Missing type hints
    for item in data:
        if threshold:
            if item > threshold:
                if verbose:
                    print(f"Item {item} exceeds threshold")
                result.append(item)
        else:
            # Deep nesting
            if item > 0:
                if item < 100:
                    if item % 2 == 0:
                        result.append(item)
                    else:
                        if item % 3 == 0:
                            result.append(item * 2)

    # Complex logic
    if len(result) > 10:
        return sorted(result)
    elif len(result) > 5:
        return result[:5]
    else:
        return result * 2


class DataProcessor:
    """Example class for analysis."""

    def __init__(self, config: dict[str, any]):
        """Initialize processor with configuration."""
        self.config = config
        self.data: list[dict] = []
        self.results: dict[str, any] = {}

    def load_data(self, source: str) -> None:
        """Load data from source."""
        # Simulate loading
        self.data = [{"id": i, "value": i * 10} for i in range(100)]

    def process(self) -> dict[str, any]:
        """Process loaded data."""
        if not self.data:
            raise ValueError("No data loaded")

        # Processing steps
        filtered = self._filter_data()
        transformed = self._transform_data(filtered)
        aggregated = self._aggregate_results(transformed)

        self.results = aggregated
        return self.results

    def _filter_data(self) -> list[dict]:
        """Filter data based on criteria."""
        threshold = self.config.get("threshold", 50)
        return [item for item in self.data if item["value"] > threshold]

    def _transform_data(self, data: list[dict]) -> list[dict]:
        """Transform filtered data."""
        multiplier = self.config.get("multiplier", 1.0)
        return [
            {
                "id": item["id"],
                "value": item["value"] * multiplier,
                "category": self._categorize(item["value"]),
            }
            for item in data
        ]

    def _categorize(self, value: float) -> str:
        """Categorize value."""
        if value < 100:
            return "low"
        elif value < 500:
            return "medium"
        else:
            return "high"

    def _aggregate_results(self, data: list[dict]) -> dict[str, any]:
        """Aggregate transformed results."""
        categories = {}
        total = 0

        for item in data:
            cat = item["category"]
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += 1
            total += item["value"]

        return {
            "total": total,
            "count": len(data),
            "average": total / len(data) if data else 0,
            "by_category": categories,
        }


def poorly_written_function(a, b, c, d, e, f):
    """Example of a poorly written function for analysis."""
    x = a + b
    if x > 10:
        if c > 5:
            if d:  # Should use 'if d:'
                for i in range(e):
                    if f[i] > 0:
                        x = x + f[i]
                    else:
                        if f[i] < -10:
                            x = x - f[i]
                        else:
                            x = x * 2
            else:
                x = x / 2
        else:
            x = x * c
    else:
        if b > a:
            x = b - a
        else:
            x = a - b

    # More issues: unused variables, magic numbers

    return x * 100  # Magic number


if __name__ == "__main__":
    main()
