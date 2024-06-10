#!/usr/bin/env python3
"""counts the delay time"""
import asyncio
import random
import time


async def wait_random(max_delay=10):
    """an asynchronous coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay
    seconds and eventually returns it"""
    current_time = time.time()
    await asyncio.sleep(random.uniform(0, max_delay))
    delay_time = time.time() - current_time
    return delay_time
