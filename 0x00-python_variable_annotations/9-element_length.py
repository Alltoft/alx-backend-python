#!/usr/bin/env python3
"""It's a type-annotated function element_length that takes a list input_list
of strings and returns a list of tuples, where each tuple contains a string
and its length."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
        lst (Iterable[Sequence]): The list of elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing each element
        and its length.
    """
    return [(i, len(i)) for i in lst]
