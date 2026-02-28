#!/usr/bin/env python3
"""Type-annotated function to return a key and squared value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    return (k, float(v * v))
