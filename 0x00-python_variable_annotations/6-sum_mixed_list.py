#!/usr/bin/env python3
"""It's a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    Calculate the sum of a mixed list of floats and integers.

    Args:
        mxd_lst (List[Union[float, int]]): The mixed list of floats and
        integers.

    Returns:
        float: The sum of the elements in the mixed list.
    """
    return sum(mxd_lst)
