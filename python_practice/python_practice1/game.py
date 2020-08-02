"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""

#定义一个fight方法：
def fight():
    # 定义四个变量，分别是代表我的血量和攻击力，你的血量和攻击力，双方攻击力的初始值都为200
    my_hp = 1200
    my_power = 200
    your_hp = 1000
    your_power = 200
    # 死循环，若不退出整个循环，将一直执行命令
    while True:
        # 定义打斗多个回合后，我的剩余血量以及你的剩余血量
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        # if...elif...语句判断
        #当我的剩余血量<=0时，打印双方的剩余血量并输出我输了，退出整个循环
        if my_hp <= 0:
            # 输出你的剩余血量和我的剩余血量，并给出判断结果
            print("你的剩余的血量是：",your_hp)
            print("我的剩余的血量是：", my_hp)
            print("我输了")
            # 跳出所有循环
            break
        # 当你的剩余血量<=0时，打印双方的剩余血量并输出你输了，退出整个循环
        elif your_hp <=0:
            # 输出我的剩余血量和你的剩余血量，并给出判断结果
            print("我的剩余的血量是：", my_hp)
            print("你的剩余的血量是：", your_hp)
            print("你输了")
            # 跳出所有循环
            break
# 调用fight()方法
fight()