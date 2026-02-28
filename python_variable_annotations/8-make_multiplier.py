#!/usr/bin/env python3
"""Type-annotated function that returns a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    def multiply(value: float) -> float:
        return value * multiplier

    return multiply
