# -*- coding:utf-8 -*-
# @Time    : 2020/10/28 10:14
# @Author  : Nicole
# @File    : student.py

class Student:
    # 类内定义的类变量
    nationality = "China"

    # 构造函数
    def __init__(self, name, gender, stu_num, grade, class_name):
        self.name = name
        self.gender = gender
        self.stu_num = stu_num
        self.grade = grade
        self.class_name = class_name

    # 动态方法 回答问题
    def answer(self):
        print(f"{self.name} is answering the question.")

    # 获取个人基本信息
    def getinfo(self):
        print(f"The basic info of {self.name} as below: \n"
              f"nationality: {self.nationality}, "
              f"gender: {self.gender}, "
              f"student NO.:{self.stu_num}, Class:{self.class_name}, Grade:{self.grade}.")

    # 开设课程情况
    def classname(self):
        classname = ["Chinese", "Math", "English"]
        print(f"{self.name} will study {classname}.")

student_A = Student("Tom", "male", "001", "2", "1")
student_A.answer()
student_B = Student("Lucy", "female", "002", "3", "2")
student_B.getinfo()
student_B.classname()

