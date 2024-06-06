#!/usr/bin/env python3
"""It's a type-annotated function safe_first_element that takes a list lst
of any type and returns its first element if it exists, otherwise None."""
from typing import Sequence, Union, Any, Optional


NoneType = Optional[Any]


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Return the first element of a list if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
