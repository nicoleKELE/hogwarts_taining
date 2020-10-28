# -*- coding:utf-8 -*-
# @Time    : 2020/10/28 15:54
# @Author  : Nicole
# @File    : car.py

class Car:
    # 构造函数
    def __init__(self, brand, type, price, color = "white"):
        self.brand = brand
        self.type = type
        self.color = color
        self.price = price

    # 动态方法 汽车刷漆
    def paint(self):
        print(f"paint the car {self.color}.")

    # 获取汽车信息
    def getinfo(self):
        print(f"Price for {self.type} of {self.brand} is {self.price}, and its color is {self.color}.")

car_A = Car(brand = "Benz", type = "MPV", price = "500000")
car_A.getinfo()
car_B = Car(brand = "Benz", type = "MPV", price = "500000", color = "black")
car_B.paint()
