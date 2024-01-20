# -*- coding: utf-8 -*-
#
# Time: 2024-01-19
# File: queue_example.py
# URL: https://www.pythontutorial.net/python-concurrency/python-thread-queue/
# Description: sample code

import time
from threading import Thread, Event
from queue import Empty, Queue


def producer(queue, event):
    for i in range(1, 6):
        print(f"Inserting item {i} into queue...")
        time.sleep(1)
        queue.put(i)

    # event.set()


def consumer(queue, event):
    # while not event.is_set():
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f"Consuming item {item} from queue...")
            time.sleep(2)
            queue.task_done()


def main():
    queue = Queue()
    event = Event()

    producer_thread = Thread(
        target=producer,
        args=(queue, event)
    )
    consumer_thread = Thread(
        target=consumer,
        args=(queue, event),
        daemon=True
    )

    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
    queue.join()


if __name__ == "__main__":
    main()
