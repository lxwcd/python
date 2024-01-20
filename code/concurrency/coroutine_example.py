# -*- coding: utf-8 -*-
#
# Time: 2024-01-19
# File: coroutine_example.py
# URL: https://www.pythontutorial.net/python-concurrency/python-async-await/
# Description: sample code

import asyncio


async def square(number):
    return number ** 2

async def foo(text):
    print(text)
    await asyncio.sleep(5)
    print("foo finished")

async def main() -> None:
    print("Start main")
    task = asyncio.create_task(foo("foo"))
    # await task
    print("End main")
    # x = await square(5)
    # print("x = ", x)
    #
    # y = await square(6)
    # print("y = ", y)
    #
    # print(f"total={x+y}")
    #
    # print("End main")

if __name__ == "__main__":
    asyncio.run(main())