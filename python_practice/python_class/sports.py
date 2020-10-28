# -*- coding:utf-8 -*-
# @Time    : 2020/10/28 16:21
# @Author  : Nicole
# @File    : sports.py

class Sports:
    # 类内定义变量
    type = ["aerobic", "anaerobic"]

    # 动态方法 体育运动项目
    def running(self):
        print(f"Running is one kind of {self.type[0]}.")
    def weightlifting(self):
        print(f"Weightlifting is belong to {self.type[1]}.")

sport_A = Sports()
sport_A.running()
sport_A.weightlifting()