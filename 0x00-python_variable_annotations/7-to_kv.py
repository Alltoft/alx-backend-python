#!/usr/bin/env python3
from typing import Union, Tuple
"""It's a type-annotated function to_kv which takes a string k and an int OR
float v as arguments and returns a tuple. The first element of the tuple is
the string k. The second element is the square of the int/float v and should
be annotated as a float."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key-value pair into a tuple where the value is squared.

    Args:
        k (str): The key of the pair.
        v (Union[int, float]): The value of the pair, which can be either an
        integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the key and the squared value.

    Example:
        >>> to_kv('x', 5)
        ('x', 25.0)
        >>> to_kv('y', 2.5)
        ('y', 6.25)
    """
    return (k, v * v)
