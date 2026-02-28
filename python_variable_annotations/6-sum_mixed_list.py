#!/usr/bin/env python3

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    float_convert = []

    for item in mxd_lst:
        float_convert.append(float(item))

    return sum(float_convert)
