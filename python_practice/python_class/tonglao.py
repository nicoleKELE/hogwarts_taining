# -*- coding:utf-8 -*-
# @Time    : 2020/10/29 10:56
# @Author  : Nicole
# @File    : tonglao.py
"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，
如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，
打完之后，比较双方血量。血多的一方获胜。

"""
class TongLao:
    def __init__(self, my_hp, my_power):
        self.my_hp = my_hp
        self.my_power = my_power

    def see_people(self, name):
        if name == "WYZ":
            print(f"师弟！！！")
        elif name == "李秋水":
            print(f"师弟是我的！")
        elif name == "丁春秋":
            print(f"叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        self.my_hp = self.my_hp + self.my_hp * 10
        self.my_power = self.my_power - self.my_power * 2
        my_final_hp = self.my_hp - enemy_power
        enemy_final_hp = enemy_hp - self.my_power
        print("I win! ") if my_final_hp > enemy_hp else print("I loose! ")

if __name__ == "__main__":
    tonglao = TongLao(1000, 200)
    tonglao.see_people("李秋水")
    tonglao.see_people("WYZ")
    tonglao.see_people("丁春秋")
    tonglao.fight_zms(20000, 600)
    tonglao.fight_zms(20000, 500)

