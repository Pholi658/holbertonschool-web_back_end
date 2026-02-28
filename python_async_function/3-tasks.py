#!/usr/bin/env python3
"""Create an asyncio.Task from wait_random coroutine."""

import asyncio
import importlib

# Import wait_random safely
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that runs wait_random(max_delay)."""
    return asyncio.create_task(wait_random(max_delay))
