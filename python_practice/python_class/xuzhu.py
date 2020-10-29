# -*- coding:utf-8 -*-
# @Time    : 2020/10/29 11:19
# @Author  : Nicole
# @File    : xuzhu.py
"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
from hogwarts_taining.python_practice.python_class.tonglao import TongLao


class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")

xuzhu = XuZhu("2000", "500")
xuzhu.read()