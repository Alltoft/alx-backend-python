#!/usr/bin/env python3
"""this func should measure the total runtime and return it"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """a coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather."""
    current_time = time.time()
    Ac = async_comprehension()
    await asyncio.gather(Ac, Ac, Ac, Ac)
    total_time = time.time() - current_time
    return total_time
