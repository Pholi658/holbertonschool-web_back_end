#!/usr/bin/env python3
"""Use async comprehension to collect numbers from async_generator."""

import importlib

# Import async_generator from the previous file
async_generator = importlib.import_module("0-async_generator").async_generator


async def async_comprehension() -> list[float]:
    """Collect 10 numbers from async_generator using async comprehension."""
    numbers = [num async for num in async_generator()]
    return numbers
