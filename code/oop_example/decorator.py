# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: decorator.py
# URL: https://python-course.eu/oop/count-function-calls-with-help-metaclass.php
# Description: sample code

def decorator(func):
    print("装饰器函数内的代码执行1")

    def wrapper(*args, **kwargs):
        print("包裹函数内的代码执行")
        return func(*args, **kwargs)

    print("装饰器函数内的代码执行2")
    return wrapper


@decorator
def target_function():
    print("目标函数内的代码执行")


def test_decorator():
    target_function()
    print('+' * 20)
    target_function()


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__

    return helper


@call_counter
def f():
    pass


def test_call_counter():
    call_counter(f)
    print(f.calls)

    for _ in range(10):
        f()

    print(f.calls)


if __name__ == '__main__':
    test_decorator()
    print('\n' + '=' * 30 + '\n')
    test_call_counter()
