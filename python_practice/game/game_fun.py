# -*- coding:utf-8 -*-
# @Time    : 2020/10/22 17:40
# @Author  : Nicole
# @File    : game_fun.py
import random

# 定义fight函数实现游戏逻辑
def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200

    # 打印敌人的血量和攻击力
    print("敌人的血量为{0}， 攻击力为{1}".format(enemy_hp, enemy_power))

    # 加入循环，让游戏可以进行多伦
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print("我的剩余血量为{}".format(my_hp))
            print("敌人的剩余血量为{}".format(enemy_hp))
            print("我输了")
            break
        elif enemy_hp <= 0:
            print("我的剩余血量{}".format(my_hp))
            print("敌人的剩余血量{}".format(enemy_hp))
            print("我赢了")
            break

if __name__=="__main__":
    hp = [x for x in range(990, 1010)]
    # 让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)

    # 敌人的攻击力用randint方法随机挑选一个值
    enemy_power = random.randint(190, 210)
    print(fight(enemy_hp, enemy_power))



