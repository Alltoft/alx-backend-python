#!/usr/bin/env python3
"""It's a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(sum_mixed_list: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all the elements in a list.

    Args:
        sum_mixed_list (List[Union[int, float]]): A list of integers and
        floats.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return sum(sum_mixed_list)
