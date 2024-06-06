#!/usr/bin/env python3
"""It's a type-annotated function safe_first_element that takes a list lst
of any type and returns its first element if it exists, otherwise None."""
from typing import List, Union, Any


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """Find the first element of a list."""
    if lst:
        return lst[0]
    else:
        return None
