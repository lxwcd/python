# -*- coding: utf-8 -*-
#
# Time: 2024-01-14
# File: csv_io.py
# URL: https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第23课：用Python读写CSV文件.md
# Description: sample code

import csv
import random
import os
import shutil
import textwrap

# 新建文件夹
folder_path = "./test_files"

if os.path.exists(folder_path):
    shutil.rmtree(folder_path)  # 存在则删除

os.makedirs(folder_path)

# write csv
# delimiter 为指定的分隔符，空格，而有些字段包含空格
# 为了让包含空格的字段为一个整体，将其引用
# quotechar 为定义的引用字符，这里为 |
# quoting 指定引用行为，QUOTE_MINIMAL 表示只有必要时才引用
# QUOTE_ALL 可以将所有字段全部引用
with open(os.path.join(folder_path, "eggs.csv"), mode="w", newline='') as f:
    spamwriter = csv.writer(f, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['spam'] * 5 + ['Backed Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# 指定 quotechar 可以将字段的引用去掉
with open(os.path.join(folder_path, "eggs.csv"), newline='') as f:
    spamwriter = csv.reader(f, delimiter=' ', quotechar='|')
    for row in spamwriter:
        print(', '.join(row))


""" example 2 """
with open(os.path.join(folder_path, "scores.csv"), mode="w", newline='') as f:
    score_writer = csv.writer(f, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL)
    score_writer.writerow(['Name', 'Chinese', 'Math', 'English'])
    names = ['Alice', 'Bob', 'Colo', 'David', 'Ele']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        score_writer.writerow(scores)

with open(os.path.join(folder_path, "scores.csv"), mode="r", newline='') as f:
    score_reader = csv.reader(f, delimiter='|', quotechar='"')
    for row in score_reader:
        row.insert(0, str(score_reader.line_num)) # 插入行号
        print('|'.join(row))

# 删除非空文件夹
shutil.rmtree("./test_files")
