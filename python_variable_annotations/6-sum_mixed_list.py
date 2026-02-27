#!/usr/bin/env python3

def sum_mixed_list(mxd_lst: list[int | float])->float:
    float_convert = []
    for item in mxd_lst:
        appended = float(item)
        float_convert.append(item)
        
    return sum(float_convert)
