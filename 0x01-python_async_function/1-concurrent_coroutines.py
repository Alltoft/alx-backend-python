#!/usr/bin/env python3
"""call delay func multiple times"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n takes in 2 int arguments will spawn wait_random
    n times with the specified max_delay"""
    Lst = []
    delay_list = []
    for i in range(n):
        Lst.append(wait_random(max_delay))
    for k in asyncio.as_completed(Lst):
        delay_list.append(await k)
    return delay_list
