Python 学习  
      
# 资源  
> [官方文档](https://docs.python.org/3/tutorial/appetite.html)  
> [Python-100-Days](https://github.com/jackfrued/Python-100-Days/tree/master)  
> [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624)  
> [Learn Python Programming](https://www.tutorialsteacher.com/python)  
> [python course](https://python-course.eu/)  
> [Python Tutorial](https://www.pythontutorial.net/)  
> Python 代码可视化生成器：[Python Tutor](https://pythontutor.com/visualize.html#mode=edit)  
> 查询特殊符号的unicode代码[unicode](https://home.unicode.org/)  
> 边框符号的unicode码[Box Drawing](https://unicode.org/charts/nameslist/n_2500.html)  
      
# 安装  
> 文档：[第01课：初识Python](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第01课：初识Python.md)  
> 视频：[Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz/?p=3&spm_id_from=pageDriver&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
## Windows 安装  
      
### 安装 python 解释器  
官网下载安装包，跟着视频安装  
      
### VSCode 配置 python  
> [Python VScode 配置](https://www.runoob.com/python3/python-vscode-setup.html)  
      
vscode 中安装插件 python  
      
### PyCharm 安装配置  
> [配置 PyCharm 设置](https://www.pycharm.net.cn/configuring-project-and-ide-settings.html)  
      
Python IDE  
      
#### 配置 vim 编辑器  
> [在 PyCharm 中使用 Vim 编辑器 (IdeaVim)](https://www.pycharm.net.cn/using-product-as-the-vim-editor.html)  
> [ideavim](https://github.com/JetBrains/ideavim?tab=readme-ov-file)  
      
如果使用自定义 vimrc 配置文件，默认路径在 `~/.ideavimrc`，家目录的位置可以在 pycharm 终端通过 `echo $HOME` 获取，如 `C:\Users\lx`  
      
#### 修改下载镜像源  
打开终端，设置 pip 安装软件的镜像源  
```bash  
pip config set global.index-url https://pypi.doubanio.com/simple  
```  
      
#### 快捷键配置  
> [配置键盘快捷键](https://www.pycharm.net.cn/configuring-keyboard-and-mouse-shortcuts.html)  
      
||||  
|:--:|:--:|:--:|  
|设置|Ctrl+Alt+S||  
|执行选择的行|Shift+E|自定义|  
|显示运行窗口|Alt+4||  
|运行选择的行|Alt+E|自定义|  
|代码格式化|Ctrl+Alt+L||  
|文件格式化|Ctrl+Alt+Shift+L||  
      
      
#### 安装 IPython  
IPython（即交互式 Python）是一个用于 Python 的交互式命令行界面，它相比标准的 Python shell 提供了增强的功能和特性。  
      
```bash  
pip install ipython  
```  
      
终端输入 `ipython` 进入该交互式环境  
      
# 代码规范  
> [4.9. Intermezzo: Coding Style](https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style)  
      
# 基本语法规则  
> [2. Lexical analysis](https://docs.python.org/3/reference/lexical_analysis.html#line-structure)  
      
## 书写多行  
> [2.1.5. Explicit line joining](https://docs.python.org/3/reference/lexical_analysis.html#explicit-line-joining)  
      
      
### 多行注释  
```python  
# comment  
      
"""  
comment line  
comment line  
"""  
```  
      
### 非字符串和注释多物理行合并为逻辑行  
```python  
# 以反斜杠（/）结尾  
      
if 1900 < year < 2100 and 1 <= month <= 12 \  
   and 1 <= day <= 31 and 0 <= hour < 24 \  
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date  
        return 1  
```  
      
Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without using backslashes.  
```python  
month_names = ['Januari', 'Februari', 'Maart',      # These are the  
               'April',   'Mei',      'Juni',       # Dutch names  
               'Juli',    'Augustus', 'September',  # for the months  
               'Oktober', 'November', 'December']   # of the year  
```  
      
### 多行字符串  
One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.  
      
```python  
print("""\  
Usage: thingy [OPTIONS]  
     -h                        Display this usage message  
     -H hostname               Hostname to connect to  
""")  
```  
      
每行末尾自动加上换行符，第一行加上 `\`可防止夹换行符  
      
如果书写时每行左侧有缩进，可以用  textwrap.dedent() 方法去掉每行开头的空格，见 [textwrap.dedent(text)](https://docs.python.org/3.12/library/textwrap.html#textwrap.dedent)  
      
# 数据类型和变量  
> [3. An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)  
> [数据类型和变量](https://www.liaoxuefeng.com/wiki/1016959663602400/1017063826246112)  
> [第03课：Python语言元素之变量](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第03课：Python语言元素之变量.md)  
> [Built-in Types](https://docs.python.org/3/library/stdtypes.html#)  
> [字符串和编码](https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896)  
      
      
## 字符串  
      
### f-string  
> [f-string](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)  
      
### str.format 字符串格式化  
> [7.1.2. The String format() Method](https://docs.python.org/3/tutorial/inputoutput.html#the-string-format-method)  
> [Python format 格式化函数](https://www.runoob.com/python/att-string-format.html)  
      
```python  
print('We are the {} who say "{}!"'.format('knights', 'Ni'))  
# We are the knights who say "Ni!"  
      
print('{0} and {1}'.format('spam', 'eggs'))  
# spam and eggs  
      
print('{1} and {0}'.format('spam', 'eggs'))  
# eggs and spam  
      
print('This {food} is {adjective}.'.format(  
      food='spam', adjective='absolutely horrible'))  
# This spam is absolutely horrible.  
```  
```python  
def __str__(self):  
    """  
    :lines: 第一个参数为数字，占两位，左对齐，除了 10 其他只占用一个字符宽度  
    :lines: 第二个参数为数字，占一位，花色图案  
    :lines: 第三个参数为数字，占两位，右对齐，除了 10 其他只占用一个字符宽度  
    """  
    lines = """\  
    ┌───────┐  
    |{}     |  
    |       |  
    |   {}  |  
    |       |  
    |     {}|  
    └───────┘  
    """.format('{rank: <2}', '{suit_value: <2}', '{rank: >2}')  
      
    # 另一种方式，书写不美观，且麻烦  
    # lines = [[] for i in range(7)]  
    # space = '' if self.rank == '10' else ' '  
    # lines[0].append('┌───────┐')  
    # lines[1].append('|{}{}     |'.format(self.rank, space))  
    # lines[2].append('|       |')  
    # lines[3].append('|   {}   |'.format(self.suit_value))  
    # lines[4].append('|       |')  
    # lines[5].append('|     {}{}|'.format(space, self.rank))  
    # lines[6].append('└───────┘')  
    # result = [''.join(line) for line in lines]  
    # return '\n'.join(result)  
          
    return textwrap.dedent(lines.format(rank=self.rank, suit_value=self.suit_value))  
```  
      
      
### str.join 字符串连接  
> [Python String join() Method](https://www.w3schools.com/python/ref_string_join.asp)  
      
      
### str.split 分割字符串  
> [str.split(sep=None, maxsplit=- 1)](https://docs.python.org/3/library/stdtypes.html?highlight=splitlines#str.split)  
      
      
### str.splitlines 划分多行  
> [str.splitlines](https://docs.python.org/3/library/stdtypes.html?highlight=splitlines#str.splitlines)  
      
```python  
string1 = "Hello\nWorld\n"  
lines1 = string1.splitlines()  
print(lines1)  
# 输出：['Hello', 'World']  
```  
      
### str.strip 移除字符串首部和尾部的字符  
> [str.strip([chars])](https://docs.python.org/3.12/library/stdtypes.html#str.strip)  
  
  
不指定字符则默认移除 whitespace，只能移除开头和结尾的字符，中间的不移除  
```python  
>>> '   spacious   '.strip()  
'spacious'  
>>> '   spacious     hello  '.strip()  
'spacious     hello'  
>>> '   www.example.com   '.strip('wcom')  
'   www.example.com   '  
```  
  
### str.rstrip 移除字符串尾部字符  
  
### str.lstrip 移除字符串首部字符  
  
### str.title 返回标题话的字符串  
每个单词的首字母变大写，其余字母小写  
  
```python  
>>> '~HEllO WORld++'.title()  
'~Hello World++'  
```  
  
### repr(str) 显示换行符等不可见字符  
```python  
>>> a = 'hello\t\tworld'  
>>> print(a)  
hello           world  
>>> print(repr(a))  
'hello\t\tworld'  
>>> print(str(a))  
hello           world  
```  
  
### 模板字符串 Template strings  
> [Template strings](https://docs.python.org/3.12/library/string.html#template-strings)  
  
  
```python  
>>> from string import Template  
>>> s = Template('$who likes $what')  
>>> s.substitute(who='tim', what='kung pao')  
'tim likes kung pao'  
>>> type(s)  
<class 'string.Template'>  
```  
和 shell 中使用变量相似，变量可用 ${} 包围  
```python  
>>> s1 = Template("${name}'s  $what")  
>>> str1 = s1.substitute(name='tim', what='cat')  
>>> str1  
"tim's  cat"  
```  
  
### raw string 原始字符串  
> [2.4.1. String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)  
  
Both string and bytes literals may optionally be prefixed with a letter 'r' or 'R'; such strings are called raw strings and treat backslashes as literal characters.   
  
  
字符串前面加上r表示原始字符串（raw string），这意味着字符串中的转义字符将被视为普通字符，而不会被解释为特殊字符。这在处理正则表达式、文件路径等需要保留反斜杠的情况下非常有用。  
  
```python  
# 不使用原始字符串  
string1 = "C:\path\to\file.txt"  
print(string1)  # 输出：C:\path	o\file.txt  
  
# 使用原始字符串  
string2 = r"C:\path\to\file.txt"  
print(string2)  # 输出：C:\path\to\file.txt  
```  
  
```python  
import re  
  
# 使用原始字符串r"\d+"，我们不需要对正则表达式中的反斜杠进行双重转义，因为原始字符串会将其视为普通字符。  
pattern = r"\d+"  
string = "12345"  
  
result = re.findall(pattern, string)  
print(result)  # 输出：['12345']  
```  
  
## list 列表  
      
### list.extend 扩展列表  
> [Python List extend()方法](https://www.runoob.com/python/att-list-extend.html)  
      
将一个可迭代对象（如列表、元组、集合等）中的元素逐个添加到列表中  
```python  
list1 = [1, 2, 3]  
list2 = [4, 5, 6]  
      
list1.extend(list2)  
      
print(list1) # [1, 2, 3, 4, 5, 6]  
```  
      
### list.pop 移除列表指定位置元素  
      
```python  
fruits = ['apple', 'banana', 'orange']  
      
# 移除并返回最后一个元素  
last_fruit = fruits.pop()  
print(last_fruit)  # 输出: 'orange'  
print(fruits)      # 输出: ['apple', 'banana']  
      
# 移除并返回指定位置的元素  
second_fruit = fruits.pop(1)  
print(second_fruit)  # 输出: 'banana'  
print(fruits)        # 输出: ['apple']  
```  
    
## 二进制数据类型 Bytes  
> [Bytes Object](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)  
      
    
```python  
>>> s2 = 'hello world'  
>>> s3 = s2.encode()  
>>> type(s3)  
<class 'bytes'>  
>>> print(s3)  
b'hello world'  
```  
    
```python  
>>> import base64  
>>> s = b'hello world'  
>>> type(s)  
<class 'bytes'>  
>>> print(s)  
b'hello world'  
>>> base64.b64encode(s)  
b'aGVsbG8gd29ybGQ='  
```  
    
# 切片  
> [切片](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856)  
      
```python  
a = "Hello, World!"  
print(a[2:5])  # llo  不包括右边界  
```  
      
- 列表切片  
```python  
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# 获取索引2到索引5之间的元素（不包括索引5）  
sliced_list = my_list[2:5]  
print(sliced_list)  # 输出: [3, 4, 5]  
      
# 获取从列表末尾开始的倒数两个元素 -1 为倒数第一个元素  
sliced_list = my_list[-2:]  
print(sliced_list)  # 输出: [9, 10]  
      
# 使用步长获取列表中的每第二个元素  
sliced_list = my_list[::2]  
print(sliced_list)  # 输出: [1, 3, 5, 7, 9]  
       
# 获取第一个元素到倒数第二元素  
my_list = [1, 2, 3, 4, 5]  
sliced_list = my_list[:-1]  
print(sliced_list)  # 输出: [1, 2, 3, 4]  
```  
      
- 字符串切片  
```python  
my_string = "Hello, World!"  
      
# 使用负数索引获取字符串末尾的字符  
sliced_string = my_string[-6:-1]  
print(sliced_string)  # 输出: "World"  
```  
      
- 元组切片  
```python  
my_tuple = (1, 2, 3, 4, 5)  
# 获取从索引1到索引4之间的元素（不包括索引4）  
sliced_tuple = my_tuple[1:4]  
print(sliced_tuple)  # 输出: (2, 3, 4)  
```  
      
      
# 列表生成式  
> [列表生成式](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)  
      
```python  
# 生成一个由两个元素的元组组成的列表  
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]  
print(pairs)  # 输出: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]  
      
# 生成一个由偶数构成的列表  
numbers = [x for x in range(10) if x % 2 == 0]  
print(numbers)  # 输出: [0, 2, 4, 6, 8]  
      
# 生成一个由两个字符串的组合构成的列表  
words = ['Hello', 'World', 'Python']  
combined = [x + ' ' + y for x in words for y in words if x != y]  
# 输出: ['Hello World', 'Hello Python', 'World Hello', 'World Python', 'Python Hello', 'Python World']  
print(combined)  
```  
      
```python  
result = []  
for index, line in enumerate(lines):  
    result.append(''.join(lines[index]))  
      
# 上面三行代码用下面一行代替  
result = [''.join(line) for line in lines]  
```  
      
      
```python  
def deal(self, number):  
    cards_dealt = []  
    for _ in range(number):  
        if len(self.cards) > 0:  
            card = self.cards.pop()  
            cards_dealt.append(card)  
    return cards_dealt  
      
    # 简化上面的代码为一行  
    return [self.cards.pop() for _ in range(number) if self.cards]  
```  
      
# 生成器  
> [生成器](https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128)  
      
# 表达式  
> [6. Expressions](https://docs.python.org/3/reference/expressions.html)  
      
      
## 条件表达式 conditional expression  
> [6.13. Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)  
> [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)  
      
```python  
a = 2  
b = 2  
      
if b < 5:  
    a = a + 1  
else:  
    a = 0  
      
# 等价于  
a = a + 1 if b < 5 else 0  
print (a) # 0  
```  
      
```python  
a = 2  
b = 2  
      
if b < 5:  
    a = a + 1  
      
# 等价于  
a += 1 if b < 5 else 0  
print (a) # 2  
```  
# 操作符  
      
## * 操作符  
      
### 解包操作 unpacking  
```python  
numbers = [1, 2, 3, 4, 5]  
a, *b, c = numbers  
      
print(a)  # 输出: 1  
print(b)  # 输出: [2, 3, 4]  
print(c)  # 输出: 5  
```  
      
```python  
list1 = [1, 2, 3]  
list2 = ['a', 'b', 'c']  
list3 = [True, False, True]  
      
lists = [list1, list2, list3]  
      
zipped = zip(*lists)  
      
for item in zipped:  
    print(item)  
      
"""  
(1, 'a', True)  
(2, 'b', False)  
(3, 'c', True)  
"""  
```  
      
### 可变参数  
```python  
def print_arguments(*args):  
    for arg in args:  
        print(arg)  
      
print_arguments(1, 2, 3)  # 输出: 1 2 3  
      
# 在函数定义中，`*args`将多个参数打包成一个元组 `args`。  
# 在函数调用时，`*numbers`将元组 `numbers` 解包为多个参数传递给函数。  
numbers = (4, 5, 6)  
print_arguments(*numbers)  # 输出: 4 5 6  
```  
      
```python  
def concatenate(*args):  
    return ''.join(args)  
      
result = concatenate('Hello', ' ', 'World')  
print(result)  # 输出: Hello World  
```  
      
      
# 循环和分支结构  
> [第05课：分支结构](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第05课：分支结构.md)  
> [条件判断](https://www.liaoxuefeng.com/wiki/1016959663602400/1017099478626848)  
      
      
## for 循环  
      
### 从列表第二个元素开始循环  
      
- 利用 range  
```python  
my_list = [1, 2, 3, 4, 5]  
      
# 获取列表的元素个数  
length = len(my_list)  
      
# 从第二个元素开始循环  
for i in range(1, length):  
    print(my_list[i])  
```  
      
- 利用切片  
```python  
my_list = [1, 2, 3, 4, 5]  
      
# 获取从第二个元素开始的子列表  
sub_list = my_list[1:]  
      
# 循环遍历子列表  
for element in sub_list:  
    print(element)  
```  
      
```python  
my_list = [1, 2, 3, 4, 5]  
      
# 循环遍历列表，跳过第一个元素  
for i, element in enumerate(my_list[1:]):  
    print(i, element)  
```  
      
# Python Scopes and Namespaces  
> [9.2. Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=79&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
      
1. 作用域规则：  
   - 局部作用域（Local Scope）：在函数内部定义的变量具有局部作用域，只能在函数内部访问。  
   - 嵌套作用域（Enclosing Scope）：当函数嵌套在另一个函数内部时，内部函数可以访问外部函数的变量。外部函数的作用域称为嵌套作用域。  
   - 全局作用域（Global Scope）：在模块级别定义的变量具有全局作用域，可以在模块中的任何地方访问。  
   - 内置作用域（Built-in Scope）：Python中有一些内置的名称，例如`print()`和`len()`。这些名称属于内置作用域，可以在任何地方直接访问。  
      
2. LEGB规则：Python中的名称解析遵循LEGB规则，即按照以下顺序查找名称：  
   - Local（局部）：在当前作用域内查找变量名。  
   - Enclosing（嵌套）：在嵌套作用域中查找变量名，逐级向外查找。  
   - Global（全局）：在全局作用域中查找变量名。  
   - Built-in（内置）：在内置作用域中查找变量名。  
      
   根据LEGB规则，Python会按照从内到外的顺序查找变量名，直到找到第一个匹配的名称。如果没有找到匹配的名称，将引发`NameError`异常。  
      
3. global和nonlocal关键字：  
   - `global`关键字：当在函数内部修改全局变量时，需要使用`global`关键字声明变量为全局变量，以便在函数内部进行修改。  
   - `nonlocal`关键字：当在嵌套函数内部修改嵌套作用域的变量时，需要使用`nonlocal`关键字声明变量为非局部变量。  
      
4. 静态名称解析：  
   在Python 3中，引入了类型提示和静态类型检查工具，例如mypy。这些工具可以在编译时对代码进行静态类型检查，提供更早的错误检测和自动补全。静态类型检查可以在一定程度上改变名称解析的行为，使其更静态化，并提供更准确的类型推断。  
      
Python中的作用域由文本结构确定，名称解析是在运行时动态进行的。LEGB规则指定了名称解析的优先级顺序。使用`global`和`nonlocal`关键字可以修改全局变量和嵌套作用域的变量。Python语言的演进将静态类型检查引入到编译阶段，提供了更准确的类型推断和错误检测。这些概念对于理解Python中的作用域和名称解析机制至关重要。  
      
# 函数  
> [第13课：函数和模块](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第13课：函数和模块.md)  
> [函数](https://www.liaoxuefeng.com/wiki/1016959663602400/1017105145133280)  
> [4.7. Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
      
      
## 变量的作用域  
> [4.7. Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=71&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
      
The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a global statement, or, for variables of enclosing functions, named in a nonlocal statement), although they may be referenced.  
      
      
## 默认参数  
> [4.7. Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
      
The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:  
      
```python  
def f(a, L=[]):  
    L.append(a)  
    return L  
      
print(f(1))  
print(f(2))  
print(f(3))  
```  
      
output:  
```python  
[1]  
[1, 2]  
[1, 2, 3]  
```  
      
## 特殊参数  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=80&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
> [第15课：函数使用进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第15课：函数使用进阶.md)  
> [4.8.2. Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)  
      
      
By default, arguments may be passed to a Python function either by position or explicitly by keyword.  
      
### 位置参数 positional argument  
默认参数为位置参数，调用函数时直接传递参数值  
```python  
# 标准参数可以传递参数值或 arg=value 的形式  
def standard_arg(arg):  
    print(arg)  
      
def pos_only_arg(arg, /):  
    print(arg)  
      
def kwd_only_arg(*, arg):  
    print(arg)  
      
def combined_example(pos_only, /, standard, *, kwd_only):  
    print(pos_only, standard, kwd_only)  
```  
      
Parameters following the / may be positional-or-keyword or keyword-only.  
      
      
### 关键字参数 keyword argument  
函数调用时传递参数为 name=value 形式  
      
```python  
def kwd_only_arg(*, arg):  
    print(arg)  
      
kwd_only_arg(arg=3)  
```  
      
### 可变参数 *arg  
```python  
def write_multiple_items(file, separator, *args):  
    file.write(separator.join(args))  
```  
      
*arg 传递的参数只能是位置参数，传递的参数类型为 tuple  
上面例子中前面的两个参数为位置参数，不能传递 name=value 的形式  
      
*arg 后面的参数为关键字参数  
```python  
def concat(*args, sep="/"):  
    return sep.join(args)  
      
concat("earth", "mars", "venus")  
'earth/mars/venus'  
concat("earth", "mars", "venus", sep=".")  
'earth.mars.venus'  
```  
      
### 可变参数 **kwarg  
**kwarg 传递的可变参数类型为 dictionary，参数为关键字参数  
      
```python  
def cheeseshop(kind, *arguments, **keywords):  
    print("-- Do you have any", kind, "?")  
    print("-- I'm sorry, we're all out of", kind)  
    for arg in arguments:  
        print(arg)  
    print("-" * 40)  
    for kw in keywords:  
        print(kw, ":", keywords[kw])  
```  
      
通常 *arguments 放在 **keywards 前面  
      
## 类型提示 type hint  
> [typing — Support for type hints](https://docs.python.org/3/library/typing.html)  
> [How to Use Type Hints for Multiple Return Types in Python](https://realpython.com/python-type-hints-multiple-types/)  
> [全面理解Python中的类型提示（Type Hints）](https://sikasjc.github.io/2018/07/14/type-hint-in-python/)  
      
```python  
def greeting(name: str) -> str:  
    return 'Hello ' + name  
```  
      
## Lambda 表达式  
> [4.8.6. Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)  
> [第15课：函数使用进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第15课：函数使用进阶.md)  
      
## 文档字符串 Documentation String  
> [4.8.7. Documentation Strings](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)  
      
在Python中，每个函数都可以包含一个特殊的文档字符串（Documentation String），也被称为docstring。文档字符串是函数定义的一部分，用于提供对函数的说明、描述和文档。  
      
文档字符串通常位于代码单元的定义之后，使用三重引号（单引号或双引号）括起来，以便可以跨多行编写。  
      
通过访问函数的 __doc__ 属性，可以获取该函数的文档字符串。  
      
```python  
def my_function():  
    """Do nothing, but document it.  
      
    No, really, it doesn't do anything.  
    """  
    pass  
      
# 打印函数的文档字符串  
print(my_function.__doc__)  
```  
      
## 函数注释 Function Annotations  
> [4.8.8. Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)  
      
Python函数注释（Function Annotations）是一种在函数定义中提供参数和返回值类型信息的方式。  
      
```python  
def add_numbers(a: int, b: int) -> int:  
    """Add two numbers and return the sum."""  
    return a + b  
          
# 显示函数注释信息  
print(add_numbers.__annotations__)  
```  
      
output:  
```python  
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}  
```  
      
## 高阶函数  
> [Python High Order Function](https://www.javatpoint.com/python-high-order-function)  
> [高阶函数](https://www.liaoxuefeng.com/wiki/1016959663602400/1017328655674400)  
      
      
## 装饰器  
> [第16课：函数的高级应用](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第16课：函数的高级应用.md)  
      
## 内置函数  
      
### Sequence Types — list, tuple, range  
> [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html?highlight=range#sequence-types-list-tuple-range)  
> [Python3 enumerate() 函数](https://www.runoob.com/python3/python3-func-enumerate.html)  
      
### enumerate  
> [enumerate](https://docs.python.org/3/library/functions.html#enumerate)  
      
```python  
seq = ['one', 'two', 'three']  
      
for i, element in enumerate(seq):  
    print(i, element)  
```  
输出：  
```python  
0 one  
1 two  
2 three  
```  
      
### zip  
> [zip(*iterables, strict=False)](https://docs.python.org/3/library/functions.html?highlight=zip#zip)  
      
```python  
list1 = [1, 2, 3]  
list2 = ['a', 'b', 'c']  
list3 = [True, False, True]  
      
zipped = zip(list1, list2, list3)  
      
for item in zipped:  
    print(item)  
```  
      
输出：  
```python  
(1, 'a', True)  
(2, 'b', False)  
(3, 'c', True)  
```  
      
      
元素组合过程中定义分隔符：  
```python  
list1 = [1, 2, 3]  
list2 = ['a', 'b', 'c']  
list3 = [True, False, True]  
      
zipped = zip(list1, list2, list3)  
      
result_list = ['\t\t'.join(str(item) for item in items) for items in zipped]  
      
print(result_list) # ['1\t\ta\t\tTrue', '2\t\tb\t\tFalse', '3\t\tc\t\tTrue']  
```  
      
### super  
> [Introduction to the Python super](https://www.pythontutorial.net/python-oop/python-super/)  
      
    
通过使用super()函数，我们可以在子类中方便地访问父类的属性和方法，并在需要的情况下进行重写或扩展  
```python  
class ParentClass:  
    def __init__(self):  
        self.value = 5  
    
    def some_method(self):  
        print("父类方法被调用")  
    
class ChildClass(ParentClass):  
    def __init__(self):  
        super().__init__()  # 调用父类的构造函数  
        self.child_value = 10  
    
    def some_method(self):  
        super().some_method()  # 调用父类的方法  
        print("子类方法被调用")  
    
# 创建子类对象  
child = ChildClass()  
    
# 调用子类方法  
child.some_method()  
    
    
# output  
# 父类方法被调用  
# 子类方法被调用  
```  
      
###  type 和 isinstance  
> [Difference between type and isinstance](https://python-course.eu/oop/inheritance.php)  
      
`isinstance` returns True if we compare an object either with the class it belongs to or with the superclass. Whereas the equality operator only returns True, if we compare an object with its own class.  
    
```python  
x = Robot("Marvin")  
y = PhysicianRobot("James")  
    
print(isinstance(x, Robot), isinstance(y, Robot)) # True True  
print(type(y) == Robot, type(y) == PhysicianRobot)  # False True  
```  
    
# 模块  
> [第13课：函数和模块](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第13课：函数和模块.md)  
> [6. Modules](https://docs.python.org/3/tutorial/modules.html#)  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=77&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
      
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.  
      
      
例如一个模块中有下面两个函数：  
```python  
# Fibonacci numbers module  
      
def fib(n):    # write Fibonacci series up to n  
    a, b = 0, 1  
    while a < n:  
        print(a, end=' ')  
        a, b = b, a+b  
    print()  
      
def fib2(n):   # return Fibonacci series up to n  
    result = []  
    a, b = 0, 1  
    while a < n:  
        result.append(a)  
        a, b = b, a+b  
    return result  
```  
      
      
在另一个模块中使用上述模块的函数：  
```python  
import fibo  
      
fibo.fib(1000)  
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987  
fibo.fib2(100)  
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  
fibo.__name__  
'fibo'  
```  
      
或者导入模块中特定的函数：  
```python  
from fibo import fib, fib2  
fib(500)  
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377  
```  
      
也可为模块取别名：  
```python  
import fibo as fib  
fib.fib(500)  
```  
      
为模块中的函数取别名：  
```python  
from fibo import fib as fibonacci  
fibonacci(500)  
```  
      
当前模块的名字 `__name__` 值为 `__main__`  
```python  
if __name__ == "__main__":  
    import sys  
    fib(int(sys.argv[1]))  
```  
      
## 模块搜索路径  
> [6.1.2. The Module Search Path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path)  
> [安装第三方模块](https://www.liaoxuefeng.com/wiki/1016959663602400/1017493741106496)  
      
## 包 Packages  
> [6.4. Packages](https://docs.python.org/3/tutorial/modules.html#packages)  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=78&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
      
Packages are a way of structuring Python’s module namespace by using “dotted module names”.  
      
## textwrap 文本处理模块  
> [textwrap](https://docs.python.org/3.12/library/textwrap.html)  
      
### textwrap.dedent 删除每行开头的空格  
如果书写时每行左侧有缩进，可以用  textwrap.dedent 方法去掉每行开头的空格，见 [textwrap.dedent(text)](https://docs.python.org/3.12/library/textwrap.html#textwrap.dedent)  
      
      
```python  
>>> import textwrap  
      
>>> str = """\  
...     hello  
...     world  
...     """  
>>> print(str)  
    hello  
    world  
      
>>> print(textwrap.dedent(str))  
hello  
world  
```  
  
### textwrap.indent 为行开头添加前缀  
  
  
  
      
## os 操作系统接口模块  
> [os— Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)  
      
### os.name  
The following names have currently been registered: 'posix', 'nt', 'java'.  
      
### os.system 执行命令  
```python  
import os  
      
if os.name == 'nt':  
    """ windows 操作系统 """  
    os.system('explorer') # 打开资源管理器  
    os.system('start www.baidu.com') # 打开网址  
    os.system('cls') # 清除终端  
elif os.name == 'posix':  
    """ linux 操作系统 """  
    os.system('pwd')  
    os.system('clear') # 清除终端  
```  
    
### os.path 路径操作  
      
## base64 编解码模块  
> [base64 - Base64编解码模块](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第20课：Python标准库初探.md)  
    
    
```python  
>>> s2 = 'hello world'  
>>> s3 = s2.encode()  
>>> type(s3)  
<class 'bytes'>  
>>> print(s3)  
b'hello world'  
```  
    
```python  
>>> import base64  
>>> s = b'hello world'  
>>> type(s)  
<class 'bytes'>  
>>> print(s)  
b'hello world'  
>>> ds1 = base64.b64encode(s)  
>>> print(ds1)  
b'aGVsbG8gd29ybGQ='  
```  
    
```python  
>>> ds1.decode()  
'aGVsbG8gd29ybGQ='  
>>> s4 = ds1.decode()  
>>> type(s4)  
<class 'str'>  
>>> base64.b64decode(s4)  
b'hello world'  
>>> base64.b64decode(ds1).decode()  
'hello world'  
>>> base64.b64decode(ds1)  
b'hello world'  
```  
    
## collections 容器数据类型模块  
    
    
## hashlib 哈希函数模块  
    
    
## heapq 堆排序模块  
    
## itertool 迭代工具模块  
    
    
## random 随机数模块  
> [random — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)  
      
### random.choice  
从非空序列中随机选择一个元素作为返回结果  
      
```python  
>>> import random  
>>> my_list = [1, 2, 3, 4, 5]  
>>> random_element = random.choice(my_list)  
>>> print(random_element)  
4  
```  
    
## uuid UUID 生成模块  
  
## re 正则表达式模块  
> [第30课：正则表达式的应用](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第30课：正则表达式的应用.md)  
> [Python Regex](https://www.pythontutorial.net/python-regex/)  
  
### re.match 从开头匹配  
> [re.match(pattern, string, flags=0)](https://docs.python.org/3/library/re.html?highlight=re%20compile#re.match)  
  
```python  
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
```  
  
最后可以知道 flags，和 vim 中类似，见 [re.RegexFlag](https://docs.python.org/3/library/re.html?highlight=re%20compile#re.RegexFlag)  
  
常见的有：  
- re.IGNORECASE 忽略大小写  
- re.MULTILINE 多行  
  
  
### re.compile  
> [re.compile(pattern, flags=0)](https://docs.python.org/3/library/re.html?highlight=re%20compile#re.compile)  
  
  
编译正则表达式模式，将其转换为正则表达式对象。编译后的正则表达式对象可以用于执行各种正则表达式操作，例如匹配、搜索和替换。  
  
使用compile()函数的主要好处是可以提高正则表达式的执行效率。当你需要多次使用同一个正则表达式模式时，使用compile()函数首先将其编译成正则表达式对象，然后重复使用该对象，可以避免每次都重新编译正则表达式模式的开销。  
  
```python  
import re  
  
# 编译正则表达式模式  
pattern = re.compile(r'\b[A-Z]+\b')  
  
# 在文本中搜索匹配项  
text = "HELLO world, HOW are you?"  
matches = pattern.findall(text)  
  
print(matches)  # 输出: ['HELLO', 'HOW']  
```  
  
### re.search   
搜索第一个匹配的字符串  
  
### re.findall  
  
### re.finditer  
  
### re.sub 替换  
```python  
def substitude_str():  
    text = 'two t0w tow TOO'  
    new_str = re.sub('tow|t0w|too', 'two', text, flags=re.IGNORECASE)  
  
    # two two two two  
    print(new_str)  
```  
  
### re.split 拆分字符  
```python  
def split_str():  
    pattern = r'\s+'  # 以一个或多个空白字符作为拆分点  
    str = "Hello   World   of    Python"  
    result = re.split(pattern, str)  
  
    print("split:")  
    for part in result:  
        print(part)  
```  
  
# 错误和异常  
> [8. Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)  
> [错误处理](https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736)  
      
## try  
      
## raise  
      
  
## with  
> [8.5. The with statement](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)  
> [Python with 关键字](https://www.runoob.com/python3/python-with.html)  
  
```python  
  
```  
  
  
# 面向对象编程  
> [Object Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)  
    
    
# 类  
> [9. Classes](https://docs.python.org/3/tutorial/classes.html)  
> [第17课：面向对象编程入门](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第17课：面向对象编程入门.md)  
> [面向对象编程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528)  
      
## 访问限制  
> [访问限制](https://www.liaoxuefeng.com/wiki/1016959663602400/1017496679217440)  
> [Python - Public, Protected, Private Members](https://www.tutorialsteacher.com/python/public-private-protected-modifiers)  
> [Public, - Protected-, and Private Attributes](https://python-course.eu/oop/object-oriented-programming.php)  
      
      
## 类变量和实例变量  
> [python class variables](https://pynative.com/python-class-variables/)  
> [9.3.5. Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)  
> [Class Variables, Attributes, and Properties](https://diveintopython.org/learn/classes/variables)  
      
      
类变量可以直接通过类名访问，而不用创建实例  
```python  
class MyClass:  
    class_var = 10  # 类变量  
      
    def __init__(self, instance_var):  
        self.instance_var = instance_var  # 实例变量  
      
      
# 通过类名访问类变量  
print(MyClass.class_var)  # 输出: 10  
      
# 创建类的实例  
obj1 = MyClass(20)  
obj2 = MyClass(30)  
      
# 访问实例变量  
print(obj1.instance_var)  # 输出: 20  
print(obj2.instance_var)  # 输出: 30  
      
# 类变量是共享的，对类变量的修改会影响所有实例  
MyClass.class_var = 50  
print(obj1.class_var)  # 输出: 50  
print(obj2.class_var)  # 输出: 50  
      
# 实例变量是每个实例独立拥有的  
obj1.instance_var = 100  
print(obj1.instance_var)  # 输出: 100  
print(obj2.instance_var)  # 输出: 30  
```  
      
## @property 属性装饰器  
> [Python Property Decorator](https://www.pythontutorial.net/python-oop/python-property-decorator/)  
> [第18课：面向对象编程进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第18课：面向对象编程进阶.md)  
> [使用@property](https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208)  
      
      
      
      
## 静态方法  
> [Python Static Method Explained With Examples](https://pynative.com/python-static-method/)  
> [第18课：面向对象编程进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第18课：面向对象编程进阶.md)  
      
      
- 静态方法是一种不依赖于类实例的方法，因此它可以在不创建类实例的情况下直接通过类来调用  
- 如果一个类中某个方法的实现与类无关，可以用 @staticmethod 装饰器使其称为静态方法，这样也能节约空间  
- 一个静态方法调用另一个静态方法  
```python  
class MyClass:  
    @staticmethod  
    def static_method1():  
        print("This is static_method1")  
            
        # Calling static_method2 from static_method1  
        MyClass.static_method2()  
        
    @staticmethod  
    def static_method2():  
        print("This is static_method2")  
            
    
# Calling static_method1 directly from the class  
MyClass.static_method1()  
    
# output  
# This is static_method1  
# This is static_method2  
```  
    
    
    
      
## 类方法 @classmethod  
> [Meaning of @classmethod and @staticmethod for beginner [duplicate]](https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner)  
> [Python零基础教程快速上手_全程干货+实用技巧小白必看](https://www.bilibili.com/video/BV1FT4y1R7sz?p=92&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
      
    
## 继承 inheritance  
> [](https://python-course.eu/oop/inheritance.php)  
    
    
      
      
## 抽象基类 ABC  
> [19. The 'ABC' of Abstract Base Classes](https://python-course.eu/oop/the-abc-of-abstract-base-classes.php)  
> 例子：[工资结算系统](https://www.bilibili.com/video/BV1FT4y1R7sz/?p=101&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
    
    
- 类似 C++ 中的抽象基类，需要导入 abc(abstract base class) 模块  
- Abstract classes are classes that contain one or more abstract methods.  
- An abstract method is a method that is declared, but contains no implementation.  
- Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.  
- 抽象方法用装饰器 @abstractmethod，抽象不像 C++ 中的纯虚函数，python 中的 abstract method 可以实现，但子子类中必须 override，子类中可以用 super() 方法来调用抽象基类的抽象方法  
    
    
## 枚举类  
> [Build Enumerations of Constants With Python's Enum](https://realpython.com/python-enum/)  
      
## 元类 metaclass  
> [使用元类](https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072)  
      
      
## 魔术方法 Magic Methods  
> [7. Magic Methods](https://python-course.eu/oop/magic-methods.php)  
> [魔术方法大全（一）——基础篇](https://www.bilibili.com/video/BV1b84y1e7hG/?spm_id_from=333.999.0.0&vd_source=a99dfd145a3e6aa8000930c149d4bf58)  
    
    
### __new__ 和 __init__  
      
### __str__ 和 __repr__  
> [How To Use the __str__() and __repr__() Methods in Python](https://www.digitalocean.com/community/tutorials/python-str-repr-functions)  
> [Easy Syntax in Python : __STR__ Vs __REPR__ Functions](https://www.youtube.com/watch?v=uKmfhJA76Y4&ab_channel=BekBrace)  
> [__str__ and __repr__ Methods](https://python-course.eu/oop/object-oriented-programming.php)  
      
```python  
class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
      
    def __str__(self):  
        return f"Point({self.x}, {self.y})"  
      
    def __repr__(self):  
        return f"Point(x={self.x}, y={self.y})"  
      
point = Point(3, 4)  
      
print(point)  # Output: Point(3, 4)  
print(str(point))  # Output: Point(3, 4)  
      
print(repr(point))  # Output: Point(x=3, y=4)  
print(point.__repr__())  # Output: Point(x=3, y=4)  
```  
  
```python  
>>> a = 'hello\t\tworld'  
>>> print(a)  
hello           world  
>>> print(repr(a))  
'hello\t\tworld'  
>>> print(str(a))  
hello           world  
```  
  
      
## 运算符重载  
> [operator — Standard operators as functions](https://docs.python.org/3/library/operator.html)  
> [How to implement __lt__ in Python?](https://pencilprogrammer.com/__lt__-python/)  
      
      
```python  
class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
      
    def __lt__(self, other):  
        return self.x < other.x and self.y < other.y  
      
# 创建两个 Point 对象  
point1 = Point(1, 2)  
point2 = Point(3, 4)  
      
# 使用 < 运算符比较两个对象  
print(point1 < point2)  # 输出: True  
```  
      
    
# 文件读写  
> [第21课：文件读写和异常处理](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第21课：文件读写和异常处理.md)  
> [29. File Management](https://python-course.eu/python-tutorial/file-management.php)  
    
  
## CSV 文件读写  
> [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)  
  
更专业数据分析用 pandas 库  
  
## word 文件操作  
> [第26课：用Python操作Word和PowerPoint](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第26课：用Python操作Word文件和PowerPoint.md)  
  
  
## pdf 文件操作  
> [第27课：用Python操作PDF文件](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第27课：用Python操作PDF文件.md)  
  
  
## 发送邮件  
  
  
  
  
# 数据分析  
> [Numerical Programming with Python](https://python-course.eu/numerical-programming/)  
  
  
# python 爬虫  
> 微信公众号内容：[learn_python3_spider](https://github.com/wistbean/learn_python3_spider?tab=readme-ov-file)  
  
  
    
# 代码示例  
      
## 21 点扑克牌游戏  
> 代码：[code](../code/card_game/blackjack.py)  
      
解释器： python3.10.6  
效果：  
![](img/2024-01-13-09-51-27.png)  
![](img/2024-01-13-09-52-00.png)  
