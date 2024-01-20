# -*- coding: utf-8 -*-
#
# Time: 2024-01-19
# File: event.py
# URL: https://www.pythontutorial.net/python-concurrency/python-stop-thread/
# Description: sample code

from threading import Thread, Event
from time import sleep

"""
主线程中控制子线程的终止。
利用 Event 类中 set() 和 is_set()
如果事件的内部标志为 True，表示事件已经被设置，is_set() 返回 True。
如果事件的内部标志为 False，表示事件未被设置，is_set() 返回 False。

In the Event class, the set() method sets the internal flag to True 
while the clear() method resets the flag to False. Also, 
the is_set() method returns True if the internal flag is set to True.
"""


def task(event: Event) -> None:
    for i in range(6):
        print(f'Running #{i + 1}')
        sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread was stopped maturely.')


def main() -> None:
    event = Event()
    thread = Thread(target=task, args=(event,))

    # start the thread
    thread.start()

    # suspend the thread after 3 seconds
    sleep(3)

    # stop the child thread
    event.set()


if __name__ == '__main__':
    main()
