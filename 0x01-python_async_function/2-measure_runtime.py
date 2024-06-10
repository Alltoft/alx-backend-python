#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function with integers as arguments that measures
    the total execution time and returns total_time / n"""

    Current_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - Current_time
    return total_time / n
