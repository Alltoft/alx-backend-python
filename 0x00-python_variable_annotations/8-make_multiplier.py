#!/usr/bin/env python3
"""Implement a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a float by
multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a given number by the specified
    multiplier.

    Args:
        multiplier (float): The multiplier to be used for multiplication.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
        returns the result of multiplying it by the multiplier.
    """
    def func(multiple: float) -> float:
        """
        Multiplies the given number by the multiplier.

        Args:
            multiple (float): The number to be multiplied.

        Returns:
            float: The result of multiplying the number by the multiplier.
        """
        return multiple * multiplier

    return func
