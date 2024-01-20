# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: timer.py
# URL: https://python-course.eu/advanced-python/recursive-functions.php
# Description: sample code

from timeit import Timer


def test_fib():
    t1 = Timer("fib(10)", "from fibonacci import fib")

    for i in range(1, 20):
        cmd = "fib(" + str(i) + ")"
        t1 = Timer(cmd, "from fibonacci import fib")
        # 执行 3 次的时间返回给 time1
        time1 = t1.timeit(3)
        cmd = "fibi(" + str(i) + ")"
        t2 = Timer(cmd, "from fibonacci import fibi")
        time2 = t2.timeit(3)
        print(f"n={i:2d}, fib: {time1:8.6f}, fibi:  {time2:7.6f}, time1/time2: {time1 / time2:10.2f}")


def test_cmd():
    t = Timer(stmt='for i in range(1000): pass')
    exec_time = t.timeit(number=100)
    average_time = exec_time / 100
    print(f"平均执行时间: {average_time} 秒")


def test_func():
    t = Timer(stmt='my_function()', setup='from my_module import my_function')
    execution_time = t.timeit()
    print(f"执行时间: {execution_time} 秒")


if __name__ == '__main__':
    test_cmd()
