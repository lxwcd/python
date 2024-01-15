# -*- coding: utf-8 -*-
#
# Time: 2024-01-15
# File: re_test.py
# URL: https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第30课：正则表达式的应用.md
# 正则表达式测试：https://regexr.com/
# Description: sample code


import re
import textwrap


def test_match():
    pattern = r'hello'

    # 多次用到 pattern 可以用 compile 将其编译为正则表达式对象
    pattern_obj = re.compile(r'hello')

    str = """\
    hello hello helloworld
    hello hello helloworld
    world hello helloworld
    """

    str1 = 'helloworld hello world'
    str2 = 'helloworld hello-world'

    print(f'origin string:', str)
    print(f'=' * 30)

    # 不能匹配，因为 match 只从开头匹配，上面的字符串开头有空格
    # match = re.match(pattern, str)
    # match = pattern_obj.match(str)

    # 去掉字符串首尾的空格，只能匹配第一个 hello ，后面的和第二行的均不能匹配
    # match = re.match(pattern, str.strip())

    # 去掉每行开头的空格，第二行开头仍不能匹配，match 不匹配多行
    # match = re.match(pattern, textwrap.dedent(str))

    # 即使用 MULTILINE 模式，也只能开头的 hello，不能匹配第二行的 hello
    # match = re.match(pattern, textwrap.dedent(str), re.MULTILINE)

    # 匹配 hello
    # match = re.match(pattern, str1)

    # 无法匹配，因为是 helloworld
    # match = re.fullmatch(pattern, str1)

    # search 找到第一个匹配的字符串，即使开头是空格不匹配也可以
    match = re.search(pattern, str)

    if match:
        print('full matched string: ', match.group())
        for index, group in enumerate(match.groups()):
            print(f'group {index}: {group}')

    print(f'=' * 30)

    # findall 查找所有的匹配的字符串 包括 helloworld 这种
    match_list = re.findall(pattern, str)
    # match_list = pattern_obj.findall(str)
    for s in match_list:
        print(s)

    print(f'=' * 30)

    match_iter = re.finditer(pattern, str)
    # match_iter = pattern_obj.finditer(str)
    for s in match_iter:
        # print(type(s))
        # print(s)
        print(s.group())


def validate_qq():
    """
    匹配 QQ 号
    名字：字母、数字或下划线构成且长度在6~20个字符之间
    QQ号：5~12的数字且首位不能为0
    """

    username_regex = r'^\w{6,20}$'
    qq_regex = r'^[1-9]\d{4,11}$'

    while True:
        username = input('Please enter your name '
                         '(6-20 characters, consisting of letters, '
                         'numbers, or underscores): ')
        if re.match(username_regex, username):
            break
        else:
            print('Invalid name. Please input again.')

    while True:
        qq = input('Please enter your QQ number '
                   '(5-12 digits, with the first digit not being 0): ')
        if re.fullmatch(qq_regex, qq):
            break
        else:
            print('Invalid QQ number. Please input again.')

    print('Valid name and QQ number.')


def extract_phone_nums_from_file(in_file, out_file):
    """
    从文件中提取手机号, 手机号合法且前后无数字
    根据以下是中国三大运营商手机号码的范围匹配：
    1. 中国移动（China Mobile）：
       - 号段：134、135、136、137、138、139、147、148、150、151、152、157、158、159、165（4G）、178、182、183、184、187、188、198
       - 总长度：11位

    2. 中国联通（China Unicom）：
       - 号段：130、131、132、145（上网卡）、146（4G）、155、156、166（4G）、171、175、176、185、186
       - 总长度：11位

    3. 中国电信（China Telecom）：
       - 号段：133、149（4G）、153、173、177、180、181、189、199
       - 总长度：11位
    """

    # 创建正则表达式对象 手机号前后无数字
    # (?<=\D) 为后向断言 lookbehind \D 匹配非数字, 因此匹配后面内容前面不是数字
    # (?:...)：这是一个非捕获组，用于将多个子模式组合在一起，但不捕获匹配的内容
    # (?=\D) 为前向断言 lookahead, 也可以写成否定式前向断言 negative lookahead (?!\d)
    # lookahead 写法为后面的内容匹配 \D，即非数字
    #
    pattern = re.compile(r'(?<=\D)(?:13[0-9]|14[5-9]|15[0-35-9]|166|17[0-8]|18[0-9]|19[89])'
                         r'\d{8}(?=\D)')

    found = False

    # save to file
    with open(in_file, mode='r', encoding='utf-8') as in_f, \
            open(out_file, mode='w', encoding='utf-8') as out_f:
        for line in in_f:
            matches = pattern.findall(line)
            if matches:
                found = True
                content = '\n'.join(matches) + '\n'
                print(content)
                out_f.write(content)

    if found:
        print(f"Phone numbers extracted from '{in_file}' and saved to '{out_file}'.")
    else:
        print("No phone numbers found in the input file.")


def substitude_str():
    text = 'two t0w tow TOO'
    new_str = re.sub('tow|t0w|too', 'two', text, flags=re.IGNORECASE)

    # two two two two
    print(new_str)


def split_str():
    pattern = r'\s+'  # 以一个或多个空白字符作为拆分点
    str = "Hello   World   of    Python"
    result = re.split(pattern, str)

    print("split:")
    for part in result:
        print(part)


if __name__ == '__main__':
    # validate_qq()
    # test_match()
    # substitude_str()
    split_str()
