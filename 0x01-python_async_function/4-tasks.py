#!/usr/bin/env python3
"""call delay func multiple times"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n takes in 2 int arguments will spawn wait_random
    n times with the specified max_delay"""
    Lst = []
    delay_list = []
    for i in range(n):
        Lst.append(task_wait_random(max_delay))
    for k in asyncio.as_completed(Lst):
        delay_list.append(await k)
    return delay_list
