#!/usr/bin/env python3
from typing import List
"""Implement a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float."""


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all the elements in a list.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of all the elements in the input list.
    """
    return sum(input_list)
