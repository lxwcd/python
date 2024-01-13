# -*- coding: utf-8 -*-
#
# Time: 2024-01-13
# File: salary_settlement.py
# URL: https://github.com/jackfrued/Python-Core-50-Courses/blob/master/第19课：面向对象编程应用.md#案例2工资结算系统
# 讲解视频：https://www.bilibili.com/vemployee_ideo/BV1FT4y1R7sz/?p=101&vd_source=a99dfd145a3e6aa8000930c149d4bf58
# Description: 学习用，代码来源见上面链接, 本例子学习抽象基类


from abc import ABC, abstractmethod


# 定义一个抽象基类
class Employee(ABC):

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def __init__(self, employee_id, name, working_hour=140):
        super().__init__(employee_id, name)
        self.working_hour = working_hour

    def get_salary(self):
        return 15_000


class Programmer(Employee):

    def __init__(self, employee_id, name, working_hour=160):
        super().__init__(employee_id, name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):

    def __init__(self, employee_id, name, sales=0):
        super().__init__(employee_id, name)
        self.sales = sales

    def get_salary(self):
        return 5800 + self.sales * 0.05


def main():
    emps = [
        Manager('M123', 'Alice'),
        Programmer('P111', 'Bob'),
        Programmer('P220', 'Cole'),
        Salesman('S344', 'Daisy')
    ]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(f'Input the working hour of {emp.name} for thin month：'))
        elif isinstance(emp, Salesman):
            emp.sales = float(input(f'Input the sales amount (yuan) for {emp.name} this month: '))

        print(f'The salary of {emp.name} in this month is: {emp.get_salary()} yuan')


if __name__ == "__main__":
    main()
