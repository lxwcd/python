# -*- coding: utf-8 -*-
#
# Time: 2024-01-19
# File: event.py
# URL: https://www.pythontutorial.net/python-concurrency/python-threading-event/
# Description: sample code

import os
from threading import Thread, Event
from urllib.request import urlretrieve

file_name = "rfc793.txt"
web_url = "https://www.ietf.org/rfc/"
local_folder = "./test_folders"
os.makedirs(local_folder, exist_ok=True)
local_file_path = os.path.join(local_folder, file_name)


def download_file(url, event):
    """
    _ 是一个特殊的变量名，通常用作“丢弃”值的占位符。
    urlretrieve 函数返回两个值：第一个是保存到本地的文件名（这里是 filename），
    第二个是一个元组 (filename, headers) 中的 headers 部分，表示HTTP响应头信息。
    由于 _ 作为接收者的变量名，表明这里并不关心下载过程中的HTTP响应头信息，
    仅保留并使用了实际保存的文件名。
    """
    print(f"Downloading file from {url}...")
    # filename, _ = request.urlretrieve(url, local_file_path)
    urlretrieve(url, local_file_path)

    event.set()


def process_file(event):
    print(f"Waiting for file {file_name} to be downloaded...")
    event.wait()
    print(f"File {file_name} is downloaded. Starting file processing...")

    word_count = 0
    with open(local_file_path, "r") as file:
        for line in file:
            word_count += len(line.split())

    print(f"Number of words in the file: {word_count}")


def main():
    event = Event()
    download_thread = Thread(target=download_file, args=(os.path.join(web_url, file_name), event))
    process_thread = Thread(target=process_file, args=(event,))

    download_thread.start()
    process_thread.start()

    download_thread.join()
    process_thread.join()

    os.remove(local_file_path)
    print("Main thread finished.")


if __name__ == "__main__":
    main()
