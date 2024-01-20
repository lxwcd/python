# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: generator.py
# URL: https://python-course.eu/advanced-python/generators-and-iterators.php
# Description: sample code

# ********* example 1 ****************
def gen1():
    my_generator = (x ** 2 for x in range(5))

    print(type(my_generator))
    # 通过迭代器逐个获取值
    # 输出 0 1 4 9 16
    for value in my_generator:
        print(value)

    print('=' * 30)


# ********* example 2 ****************
def gen_2():
    def gen():
        yield 1
        return 42
        yield 2

    generator = gen()
    print(next(generator))  # 输出：1
    print(next(generator))  # 输出：1

    try:
        print(next(generator))
    except StopIteration as e:
        print("StopIteration exception occurred:", e)

    print('=' * 30)


# ********* example 3 ****************
def gen_3():
    def simple_coroutine():
        print("coroutine has been started!")
        while True:
            x = yield "foo"
            print("coroutine received: ", x)

    cr = simple_coroutine()
    next(cr)
    ret_value = cr.send("Hi")
    print("'send' returned: ", ret_value)

    print('=' * 30)


# ********* example 4 ****************
def gen_4():
    def gen():
        value = yield "Ready"
        print("Received:", value)
        value = yield "Set"
        print("Received:", value)
        yield "Go"

    generator = gen()

    result = next(generator)
    print(result)  # 输出："Ready"

    result = generator.send(10)
    print(result)  # 输出："Set"

    print('=' * 30)


# ********* example 5 ****************
def gen_5():
    def count(firstval=0, step=1):
        counter = firstval
        while True:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val

    start_val = 2.1
    step = 0.3
    counter = count(start_val, step)
    for i in range(10):
        new_val = next(counter)
        print(f'{new_val:2.2f}', end='\n')
    print('set current count value to another value.')
    counter.send(100.5)
    for i in range(10):
        new_val = next(counter)
        print(f'{new_val:2.2f}', end='\n')

    print('=' * 30)


# ********* example 6 ****************
def gen_6():
    def song_generator():
        new_song = yield "First Song"
        while True:
            print("Received song:", new_song)
            new_song = yield "Next Song:"

    radio_program = song_generator()
    print(next(radio_program))  # 输出: First Song
    print(radio_program.send("Song 1"))  # 输出: Received song: Song 1, Next Song
    print(radio_program.send("Song 2"))  # 输出: Received song: Song 2, Next Song

    print('=' * 30)


# ********* example 7 ****************
def gen_7():
    from random import choice
    def song_generator(song_list):
        new_song = None
        while True:
            if new_song != None:
                if new_song not in song_list:
                    song_list.append(new_song)
                new_song = yield new_song
            else:
                new_song = yield choice(song_list)

    songs = ["Her Şeyi Yak - Sezen Aksu",
             "Bluesette - Toots Thielemans",
             "Six Marimbas - Steve Reich",
             "Riverside - Agnes Obel",
             "Not for Radio - Nas",
             "What's going on - Taste",
             "On Stream - Nils Petter Molvær",
             "La' Inta Habibi - Fayrouz",
             "Ik Leef Niet Meer Voor Jou - Marco Borsato",
             "Δέκα λεπτά - Αθηνά Ανδρεάδη"]

    radio_program = song_generator(songs)
    next(radio_program)

    for i in range(3):
        print(next(radio_program))

    radio_program.send('Distorted Angels - Archive')

    print('=' * 30)


# ********* example 8 ****************
def gen_8():
    def count(first_val=0, step=1):
        counter = first_val
        while True:
            try:
                # 每次 yield 后返回 counter 的值
                # 下次迭代时，由于没有 send 发送值，因此下次 new_counter_val 为 None
                new_counter_val = yield counter
                if new_counter_val is None:
                    counter += step
                else:
                    counter = new_counter_val
            except Exception:
                yield (first_val, step, counter)

    c = count()
    for i in range(6):
        print(next(c))

    print("Let us see what the state of the iterator is:")
    state_of_count = c.throw(Exception)
    print(state_of_count)
    print("now, we can continue:")
    for i in range(3):
        print(next(c))

    print('=' * 30)


# ********* example 9 ****************
def gen_9():
    def gen1():
        for char in 'python':
            yield char
        for num in range(5):
            yield num

    def gen2():
        yield from 'python'
        yield from range(5)

    g1 = gen1()
    g2 = gen2()
    print('g1: ', end=', ')
    for c in g1:
        print(c, end=', ')

    print('\ng2: ', end=', ')
    for n in g2:
        print(n, end=', ')

    print()
    print('=' * 30)


# ********* example 10 ****************
def gen_10():
    """递归生成器，给列表元素进行排列组合"""

    def permutations(items):
        n = len(items)
        if n == 0:
            yield []
        else:
            for i in range(len(items)):
                for cc in permutations(items[:i] + items[i + 1:]):
                    yield [items[i]] + cc

    # 示例用法
    for p in permutations(['r', 'e', 'd']):
        print(''.join(p))

    print('*' * 15)

    for p in permutations(list("game")):
        print(''.join(p), end="\n")

    print('=' * 30)


if __name__ == '__main__':
    gen_10()
