# -*- coding:utf-8 -*-
# @Time    : 2020/10/28 16:46
# @Author  : Nicole
# @File    : fruits.py

class Fruits:
    # 构造函数
    def __init__(self, name, taste, shape):
        self.name = name
        self.taste = taste
        self.shape = shape

    # 动态方法 水果基本属性介绍
    def fruitintro(self):
        print(f"{self.name} tastes {self.taste} and its shape is {self.shape}.")

apple = Fruits("apple", "sweet", "round")
apple.fruitintro()