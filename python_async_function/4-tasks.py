#!/usr/bin/env python3
"""Spawn multiple task_wait_random tasks concurrently and collect results."""

import asyncio
from typing import List
import importlib

# Import task_wait_random safely
task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn n task_wait_random tasks and return their results"""

    delays: List[float] = []

    # Spawn n tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Collect results as they finish
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
