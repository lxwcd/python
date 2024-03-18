# -*- coding: utf-8 -*-
#
# Time: 2024-01-18
# File: multi_thread.py
# URL:
# Description: sample code


import concurrent.futures
from threading import Thread
import threading
import time


# 定义一个简单的线程任务
def print_numbers(num):
    for i in range(num):
        time.sleep(1)  # 模拟耗时操作
        print(f"Thread 1: {i}", end="\n")


def print_letters(string):
    for char in string:
        time.sleep(1)  # 模拟耗时操作
        print(f"Thread 2: {char}", end="\n")


# ********* 简单多线程实现 ****************
def thread_1():
    # 创建两个线程
    threads = [
        Thread(target=print_numbers, kwargs={"num": 5}),
        Thread(target=print_letters, kwargs={"string": "python"})
    ]

    start = time.time()

    # 启动线程
    """
    start() 方法开始执行，直到线程执行完毕。
    start() 只能被调用一次。
    start() 不会阻塞主线程，而是在调用 join() 时阻塞。
    It arranges for the object’s run() method to be invoked in a separate thread of control.
    """
    for thread in threads:
        thread.start()

    print("Main Thread: after thread.start()")

    # 等待线程执行完成
    """
    当在一个线程上调用 join() 方法时，如果该线程尚未完成其执行，
    则调用此方法的线程（通常为主线程）将被阻塞，直到被调用 join() 的线程运行结束。
    """
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"time: {end - start:.3f}s")
    print('=' * 30)


# ********* daemon thread ****************
"""
By definition, daemon threads are background threads. 
In other words, daemon threads execute tasks in the background.

守护线程是一种在程序运行时在后台运行的线程。与非守护线程相反，守护线程不会阻止程序退出。
当所有非守护线程结束时，程序会等待守护线程完成其工作，然后退出。但是，如果还存在守护线程，它们可能会被强制终止。
默认情况下，主线程是非守护线程（daemon=False）
任何非守护线程启动的子线程也会是非守护线程。
只有明确将子线程设置为守护线程，它才会在进程没有其他非守护线程时随进程一起结束。
守护线程常用于执行清理工作、监控任务或其他辅助性操作，在进程不再需要服务用户请求或进行主要计算时可以随时结束。
需要注意的是，由于守护线程可能在不确定的时间点被强制结束，因此不应该用于处理需要确保完整执行的任务。
"""


def time_consume():
    while True:
        time.sleep(1)


def check_input_queue(queue):
    while True:
        answer = queue.get()  # 非阻塞式获取用户输入
        answer = answer.strip().lower()
        if answer == "y":
            print("Continue")
        elif answer == "n":
            break
        else:
            print("Please enter y or n.")


def thread_2():
    t = threading.Thread(target=time_consume, daemon=True)
    t.start()
    start = time.time()

    while True:
        answer = input("Do you want to continue? (y/n): ").strip().lower()
        if answer == "n":
            break
        elif answer == "y":
            print("Continue")
        else:
            print("Please enter y or n.")

    end = time.time()
    print(f"time: {end - start:.3f}s")
    print('=' * 30)


# ********* 自定义线程类 ****************
class CustomThread(Thread):
    def __init__(self, name, delay, count):
        super().__init__()
        self.name = name
        self.delay = delay
        self.count = count

    def run(self):
        """实现在线程启动时执行的逻辑"""
        print(f"Thread {self.name} started.")
        self.print_numbers_with_delay()
        print(f"Thread {self.name} finished.")

    def print_numbers_with_delay(self):
        for i in range(self.count):
            time.sleep(self.delay)
            print(f"{self.name}: {i}")


def thread_3():
    threads = [
        CustomThread(name="Thread 1", delay=1, count=5),
        CustomThread(name="Thread 2", delay=0.8, count=3)
    ]

    for thread in threads:
        thread.start()

    for char in "python":
        time.sleep(1)
        print(f"Main Thread: {char}")

    for thread in threads:
        thread.join()

    print("Main thread execution completed.")

    print('=' * 30)


# ********* 线程池 ****************
"""
submit(): dispatch a function to be executed and return a Future object. 
          The submit() method takes a function and executes it asynchronously.

submit 方法用于提交单个任务，并返回一个 concurrent.futures.Future 对象，该对象代表任务的未来结果。
可以通过 Future 对象来获取任务的结果或检查任务是否完成。
submit 适用于提交单个任务，返回一个 Future 对象。
submit 更适用于需要独立管理每个任务执行过程和结果的场景。

map(): execute a function asynchronously for each element in an iterable.
map 方法用于并行地对可迭代的参数执行相同的函数，返回结果列表。
它会自动将参数拆分成多个任务，并将结果按照参数的顺序返回。
map 适用于并行地对可迭代的参数执行相同的函数，返回结果列表。
map 自动管理任务的提交和结果的返回，更方便对多个参数执行相同的函数。
map 更适合于需要同时并行处理多个数据集，并确保所有任务完成后以原始顺序获得结果的情况。

shutdown(): shut down the executor
"""

from concurrent.futures import ThreadPoolExecutor


def print_numbers_with_delay(delay, count, thread_name="Thread"):
    results = []
    for i in range(count):
        time.sleep(delay)  # 模拟耗时操作
        result = f"{thread_name}: {i}"
        print(result)
        results.append(result)

    return results


def thread_4():
    with ThreadPoolExecutor(max_workers=2) as pool:
        tasks = [(1, 5, "Thread 1"), (0.800, 3, "Thread 2")]

        # 提交任务到线程池，并指定参数
        # *task 的作用是将 task 元组中的元素拆分成独立的参数传递给 pool.submit 函数
        fs = [pool.submit(print_numbers_with_delay, *task) \
              for task in tasks]

        # 主程序继续执行其他任务
        for char in "hello":
            time.sleep(1)
            print(f"Main Thread: {char}")

        # 获取任务列表的结果
        # result() 方法将会阻塞当前线程，直到有结果可用或者引发异常（如果任务执行过程中发生错误）
        results = [future.result() for future in concurrent.futures.as_completed(fs)]

    # 打印线程池中的任务结果
    print("+" * 10)
    for i, result in enumerate(results, 1):
        print(f"Thread {i} result:", result)

    print("Main thread execution completed.")


if __name__ == "__main__":
    thread_2()
