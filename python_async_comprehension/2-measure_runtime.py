#!/usr/bin/env python3


import asyncio
import time

# Import async_comprehension safely
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:

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
