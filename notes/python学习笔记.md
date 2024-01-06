Python 学习

# 资源
> [官方文档](https://docs.python.org/3/tutorial/appetite.html)
> [Python-100-Days](https://github.com/jackfrued/Python-100-Days/tree/master)
> [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624)
> Python 代码可视化生成器：[Python Tutor](https://pythontutor.com/visualize.html#mode=edit)

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
|运行选择的行|Shift+E|自定义|
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


- 多行注释
```python
# comment

"""
comment line 
comment line
"""
```

- 非字符串和注释多物理行合并为逻辑行
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

- 字符串多行
One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. 

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

# 数据类型和变量
> [3. An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)
> [数据类型和变量](https://www.liaoxuefeng.com/wiki/1016959663602400/1017063826246112)
> [第03课：Python语言元素之变量](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第03课：Python语言元素之变量.md)
> [Built-in Types](https://docs.python.org/3/library/stdtypes.html#)
> [字符串和编码](https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896)



## f-string
> [f-string](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

# 生成器
> [生产器](https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128)

# 循环和分支结构
> [第05课：分支结构](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第05课：分支结构.md)
> [条件判断](https://www.liaoxuefeng.com/wiki/1016959663602400/1017099478626848)

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

# 类
> [9. Classes](https://docs.python.org/3/tutorial/classes.html)
> [第17课：面向对象编程入门](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第17课：面向对象编程入门.md)
> [面向对象编程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528)


## @property 属性装饰器
> [Python Property Decorator](https://www.pythontutorial.net/python-oop/python-property-decorator/)
> [第18课：面向对象编程进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第18课：面向对象编程进阶.md)
> [使用@property](https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208)




## 静态类
> [Python Static Method Explained With Examples](https://pynative.com/python-static-method/)
> [第18课：面向对象编程进阶](https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第18课：面向对象编程进阶.md)


- 静态方法是一种不依赖于类实例的方法，因此它可以在不创建类实例的情况下直接通过类来调用