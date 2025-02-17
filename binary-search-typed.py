#!/usr/bin/env python3
import math
from typing import Optional

   
def foo(x: string):
    return x-1

def binary_search(l: list[int], x: int) -> Optional[int]:
    return binary_search_inner(l, x, 0, len(l) - 1)

# take care for the awkward indexing (floor and idx_left are coupled in a surprising way)
def binary_search_inner(l: list[int], x: int, idx_left: int, idx_right: int) -> Optional[int]:
    if idx_left == idx_right:
        if x == l[idx_left]:
            return idx_left
        else:
            return None
    else:
        idx = math.floor((idx_left + idx_right) / 2)
        if x < l[idx]:
            return binary_search_inner(l, x, idx_left, idx-1)
        elif x > l[idx]:
            return binary_search_inner(l, x, foo(idx), idx_right)
        else: # must be equal
            return idx



print(binary_search([0, 1, 2, 3, 4, 5, 6], 0))
