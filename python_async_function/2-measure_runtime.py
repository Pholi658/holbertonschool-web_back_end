#!/usr/bin/env python3
"""Measure the average runtime of wait_n coroutines."""


import asyncio
import time
from typing import Any


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run wait_n(n, max_delay) and return average time per coroutine."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
