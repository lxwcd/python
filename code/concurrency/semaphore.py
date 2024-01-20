# -*- coding: utf-8 -*-
#
# Time: 2024-01-19
# File: semaphore.py
# URL: https://www.pythontutorial.net/python-concurrency/python-semaphore/
# Description: sample code

import os
import shutil
import threading
from urllib.request import urlretrieve
from urllib.parse import urlparse

MAX_CONCURRENT_DOWNLOADS = 3

# create a Semaphore object and specify the number of threads
# that can acquire it at the same time
semaphore = threading.Semaphore(MAX_CONCURRENT_DOWNLOADS)

local_folder = "./test_folders"
os.makedirs(local_folder, exist_ok=True)


def download(url):
    with semaphore:
        print(f"Downloading {url}...")

        file_name = os.path.basename(urlparse(url).path)
        urlretrieve(url, os.path.join(local_folder, file_name))

        # response = urllib.request.urlopen(url)
        # data = response.read()

        print(f"Finished downloading {url}")

        # return data


def main():
    urls = [
        'https://www.ietf.org/rfc/rfc791.txt',
        'https://www.ietf.org/rfc/rfc792.txt',
        'https://www.ietf.org/rfc/rfc793.txt',
        'https://www.ietf.org/rfc/rfc794.txt',
        'https://www.ietf.org/rfc/rfc795.txt'
    ]

    threads = []

    for url in urls:
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def del_test_folders():
    shutil.rmtree(local_folder)


if __name__ == '__main__':
    main()
    # del_test_folders()
