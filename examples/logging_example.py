#!/usr/bin/env python3
"""Structured logging examples using PyDvlp Debug."""

from __future__ import annotations

import random
import time

from pydvlp.debug import debugkit, get_logger


def main():
    """Demonstrate logging features."""
    print("=== Structured Logging Examples ===\n")

    # Create logger
    logger = get_logger(__name__)

    # Example 1: Basic logging levels
    print("1. Basic logging levels:")
    logger.debug("Debug message - detailed information")
    logger.info("Info message - general information")
    logger.warning("Warning message - something to note")
    logger.error("Error message - something went wrong")
    logger.success("Success message - operation completed")

    # Example 2: Logging with context
    print("\n2. Logging with context:")
    with logger.context("user_session", user_id=12345, session_id="abc-123"):
        logger.info("User logged in")
        process_user_request(logger)
        logger.info("User session complete")

    # Example 3: Structured data logging
    print("\n3. Structured data logging:")
    logger.info(
        "Order processed",
        extra={
            "order_id": "ORD-2024-001",
            "customer_id": 98765,
            "total_amount": 125.50,
            "items_count": 3,
            "payment_method": "credit_card",
        },
    )

    # Example 4: Performance logging
    print("\n4. Performance metrics:")
    start_time = time.time()

    # Simulate work
    result = perform_calculation()

    duration = time.time() - start_time
    logger.info(
        "Calculation completed",
        extra={
            "duration_seconds": duration,
            "result_size": len(str(result)),
            "performance_metric": result / duration,
        },
    )

    # Example 5: Table logging
    print("\n5. Table logging:")
    metrics = {
        "requests_per_second": 1523,
        "average_response_time_ms": 45.2,
        "error_rate_percent": 0.03,
        "active_connections": 234,
        "memory_usage_mb": 512.3,
    }
    logger.metrics(metrics, title="System Metrics")

    # Example 6: Exception logging
    print("\n6. Exception logging:")
    try:
        risky_operation()
    except Exception:
        logger.exception("Failed to complete risky operation")

    # Example 7: Progress logging
    print("\n7. Progress logging:")
    process_batch_with_logging(logger)

    # Example 8: Using debugkit context
    print("\n8. Using debugkit context:")
    with debugkit.create_context("data_import") as ctx:
        ctx.log("Starting data import")

        for i in range(3):
            ctx.log(f"Processing batch {i + 1}/3")
            time.sleep(0.5)

        ctx.log("Data import complete", extra={"total_records": 1500})


def process_user_request(logger):
    """Process user request with logging."""
    logger.debug("Validating request parameters")

    # Simulate processing steps
    steps = ["validation", "authorization", "processing", "response"]

    for step in steps:
        logger.info(f"Executing step: {step}")
        time.sleep(0.1)  # Simulate work

        if step == "processing":
            logger.debug(
                "Processing details",
                extra={
                    "query_count": 5,
                    "cache_hits": 3,
                    "cache_misses": 2,
                },
            )


def perform_calculation():
    """Perform a calculation."""
    return sum(i**2 for i in range(1000))


def risky_operation():
    """Operation that might fail."""
    if random.random() > 0.5:
        raise ValueError("Random failure occurred")
    return "Success"


def process_batch_with_logging(logger):
    """Process items in batches with progress logging."""
    total_items = 100
    batch_size = 20

    logger.info(f"Starting batch processing of {total_items} items")

    for i in range(0, total_items, batch_size):
        batch_end = min(i + batch_size, total_items)

        # Process batch
        time.sleep(0.2)  # Simulate processing

        progress = (batch_end / total_items) * 100
        logger.info(
            "Batch processed",
            extra={
                "batch_start": i,
                "batch_end": batch_end,
                "progress_percent": progress,
                "items_processed": batch_end,
                "items_remaining": total_items - batch_end,
            },
        )

    logger.success("All batches processed successfully")


class ServiceWithLogging:
    """Example service class with integrated logging."""

    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)
        self.request_count = 0

    def handle_request(self, request_data: dict) -> dict:
        """Handle incoming request with logging."""
        request_id = f"REQ-{self.request_count:04d}"
        self.request_count += 1

        with self.logger.context("request", request_id=request_id):
            self.logger.info("Request received", extra=request_data)

            try:
                # Validate
                self._validate_request(request_data)

                # Process
                result = self._process_request(request_data)

                self.logger.success(
                    "Request completed",
                    extra={
                        "processing_time_ms": random.uniform(10, 100),
                    },
                )

                return result

            except Exception as e:
                self.logger.error(
                    "Request failed",
                    extra={"error_type": type(e).__name__, "error_message": str(e)},
                )
                raise

    def _validate_request(self, data: dict):
        """Validate request data."""
        self.logger.debug("Validating request data")

        required_fields = ["action", "payload"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

    def _process_request(self, data: dict) -> dict:
        """Process the request."""
        self.logger.debug("Processing request", extra={"action": data["action"]})

        # Simulate processing
        time.sleep(random.uniform(0.01, 0.05))

        return {
            "status": "success",
            "action": data["action"],
            "result": "processed",
        }


if __name__ == "__main__":
    main()

    # Example of service usage
    print("\n=== Service Example ===")
    service = ServiceWithLogging()

    requests = [
        {"action": "create", "payload": {"item": "example1"}},
        {"action": "update", "payload": {"item": "example2"}},
        {"action": "delete"},  # This will fail validation
    ]

    for req in requests:
        try:
            result = service.handle_request(req)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Failed: {e}")
