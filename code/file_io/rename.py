# -*- coding: utf-8 -*-
#
# Author: lx
# Time: 2024-03-05
# File: rename.py
# Description: 重命名 .png 文件

import os
import glob

# 设置图片所在的文件夹路径
folder_path = './test_files/images'

# 获取该文件夹下所有的.png文件
png_files = glob.glob(os.path.join(folder_path, '*.png'))

# 排序文件以保证重命名的连续性
png_files.sort()

# 遍历文件并进行重命名操作
for index, file_path in enumerate(png_files, start=1):
    # 构建新文件名，数字部分使用zfill保证格式为02d
    new_file_name = f"{str(index).zfill(2)}.png"
    new_file_path = os.path.join(folder_path, new_file_name)

    # 重命名文件
    os.rename(file_path, new_file_path)
    print(f"Renamed '{file_path}' to '{new_file_path}'")

# 打印完成信息
print(f"Renamed all .png files in '{folder_path}'.")