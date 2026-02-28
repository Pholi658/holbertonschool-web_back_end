#!/usr/bin/env python3


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    delays: List[float] = []

    # Create all tasks
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Collect results as they complete
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
