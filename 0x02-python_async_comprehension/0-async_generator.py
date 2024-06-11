#!/usr/bin/env python3
"""create an async_generator"""
import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> AsyncGenerator[int, None]:
    """ coroutine that takes no arguments The coroutine will loop 10 times
    each time asynchronously wait 1 second
    then yield a random number between 0 and 10 """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
