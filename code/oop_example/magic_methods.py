# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: magic_methods.py
# URL: https://python-course.eu/oop/magic-methods.php
# Description: sample code


class Length:
    __metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144,
                "mi": 1609.344}

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def converse_to_metres(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        """
        operator +
        不能处理 5 + Length(3, "yd")
        """
        if type(other) == int or type(other) == float:
            """ Length(3, "yd") + 5 """
            l = self.converse_to_metres() + other
        else:
            """ Length(3, "yd") + Length(4) """
            l = self.converse_to_metres() + other.converse_to_metres()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __radd__(self, other):
        """
        当左侧类型不支持加法运算，调用右侧的 __radd__ 方法
        处理 5 + Length(3, "yd") 情况
        """
        return Length.__add__(self, other)

    def __iadd__(self, other):
        """operator += """
        l = self.converse_to_metres() + other.converse_to_metres()
        self.value = 1 / Length.__metric[self.unit]
        return self

    def __str__(self):
        return str(self.converse_to_metres())

    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"


if __name__ == "__main__":
    x = Length(4)
    print(x)
    y = eval(repr(x))
    z = Length(4.5, "yd") + Length(1)
    print(repr(z))
    print(z)

    L = Length
    print(L(2.56, "m") + L(3, "yd") + L(7.8, "in") + L(7.03, "cm"))

    x1 = 5 + Length(3, "yd")
