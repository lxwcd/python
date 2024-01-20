# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: iter.py
# URL: https://python-course.eu/advanced-python/iterable-iterator.php
# Description: sample code

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)

print('='*20)
class MyIterator_1:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0  # 初始化索引
        self.filtered_data = [x for x in self.data if x % 2 == 0]  # 过滤数据
        return self

    def __next__(self):
        if self.index >= len(self.filtered_data):
            raise StopIteration
        value = self.filtered_data[self.index]
        self.index += 1
        return value


my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator_1(my_list)

for item in my_iterator:
    print(item)

print('='*20)
class MyIterator_2:
    def __init__(self, data):
        self.data = data
        self.index = 0  # 初始化索引
        self.filtered_data = [x for x in self.data if x % 2 == 0]  # 过滤数据

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.filtered_data):
            raise StopIteration
        value = self.filtered_data[self.index]
        self.index += 1
        return value


my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator_2(my_list)

for item in my_iterator:
    print(item)

print('='*20)

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# 使用迭代器进行遍历
for item in my_iterator:
    print(item)

print('='*20)

other_cities = ["Strasbourg", "Freiburg", "Stuttgart",
                "Vienna / Wien", "Hannover", "Berlin",
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break

print('='*20)
my_string = "Hello"
my_iterator = iter(my_string)

while my_iterator:
    try:
        character = next(my_iterator)
        print(character)
    except StopIteration:
        break