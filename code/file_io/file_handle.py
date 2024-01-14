# -*- coding: utf-8 -*-
#
# Time: 2024-01-14
# File: file_handle.py
# URL: https://python-course.eu/python-tutorial/file-management.php
# Description: sample code

import os
import shutil
import textwrap

# 新建文件夹
folder_path = "./test_files"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)  # 存在则删除

os.makedirs(folder_path)

# file read and write
definition: str = """\
    A computer file is a computer resource for recording data discretely in a
    computer storage device. Just as words can be written 
    to paper, so can information be written to a computer
    file. Files can be edited and transferred through the 
    internet on that particular computer system."""

with open("./test_files/file_definition.txt", mode="w") as f:
    f.write(textwrap.dedent(definition))  # remove leading whitespace from every line

with open("./test_files/file_definition.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # remove leading and trailing whitespace

# 获取网页文件
import requests

url = "https://python-course.eu/txt/pythonista_and_python.txt"
save_path = "./test_files/file_2.txt"  # 保存文件的本地路径和文件名
response = requests.get(url)

if response.status_code == 200:
    with open(save_path, mode="w", encoding="utf-8") as f:
        f.write(response.text)
else:
    print("Failed to get file")

# 文件替换和拷贝
with open("./test_files/file_2.txt", mode="r", encoding="utf-8") as infile:
    infile.seek(0, 2)  # 文件指针移到末尾
    print("current position (bytes of the file): ", infile.tell())
    with open("./test_files/file_3.txt", mode="w", encoding="utf-8") as outfile:
        for line in infile:
            line = line.replace("Pythonista", "Python newbie")
            line = line.replace("Python snake", "Python guru")
            print(line.rstrip())
            outfile.write(line)

# Reset the files current position
with open("./test_files/small_text.txt", mode="w", encoding="utf-8") as f:
    f.write("brown is her favorite colour")

with open("./test_files/small_text.txt") as f:
    print("current position: ", f.tell())
    print(f.read(5))
    print("current position: ", f.tell())
    print(f.read())
    print("current position: ", f.tell())

# 汉字的处理 seek 调整位置 写并读文件，用 w+ 模式而非 w 模式
poem = """\
无波真古井
有节是秋筠"""
with open("./test_files/chinese.txt", mode="w+", encoding="utf-8") as f:
    f.write(poem)
    print("current position: ", f.tell())  # 32 文件末尾
    f.seek(0)
    print("current position: ", f.tell())  # 0 文件开头
    print(repr(f.read(1)))  # 无 读一个字符而非一个字节 repr() 显示换行符
    print("current position: ", f.tell())  # 3 一个中文字占 3 字节

# Binary file read
with open("./test_files/small_text.txt", mode="rb") as f:
    print(f.read())
    print(type(f.read()))

# 删除文件
os.remove(os.path.join(folder_path, "file_definition.txt"))

# 删除非空文件夹
shutil.rmtree("./test_files")
