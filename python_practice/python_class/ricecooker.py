# -*- coding:utf-8 -*-
# @Time    : 2020/10/28 17:50
# @Author  : Nicole
# @File    : ricecooker.py

class RiceCooker:
    # 构造函数
    def __init__(self, brand, capacity, energylabel, heatup, price):
        self.brand = brand
        self.capacity = capacity
        self.energylabel = energylabel
        self.heatup = heatup
        self.price = price

    # 动态方法 电饭煲参数
    def info(self):
        print(f"The basic paramerters for {self.brand} ricecooker are: \n"
              f"capacity: {self.capacity}, energylabel: {self.energylabel}, "
              f"heatup: {self.heatup}, price: {self.price}.")

    # 煮饭煲汤
    def cooking(self):
        food = ["rice", "soup"]
        print(f"ricecooker can be used to cook {food[0]} and {food[1]}.")

ricecooker = RiceCooker("supor", "3L", "Level1", "electromagnetic heating", "300RMB")
ricecooker.info()
ricecooker.cooking()