#!/usr/bin/env python3
"""Measure runtime of multiple async_comprehension calls in parallel."""

import importlib
import asyncio
import time

# Import async_comprehension safely
async_comprehension = importlib.import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and measure total runtime."""
    
    start = time.perf_counter()
    
    # Run 4 async_comprehension calls concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end = time.perf_counter()
    
    return end - start
