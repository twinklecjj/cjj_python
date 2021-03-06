# -*-coding:utf-8-*-
"""
设定一个回合制对打游戏。
每个人物都有hp，power，skill
hp代表血量，power代表攻击力，skill将攻击力翻倍
使用yaml 配置对打的角色信息。
"""
import yaml
class Game:
    def __init__(self):
        # 定义四个变量，存放你和我的 血量还有攻击力
        data = yaml.safe_load(open("game.yml"))
        print(data)
        # 通过字典的索引获取字典的value
        self.my_hp = data["me"]["hp"]
        self.my_power =  data["me"]["power"]
        self.my_skill =  data["me"]["skill"]
        self.your_hp =  data["you"]["hp"]
        self.your_power =  data["you"]["power"]
        self.your_skill = data["you"]["skill"]

    # 快捷键 ，往前缩进是tab + shift ，往后缩进是tab
    def fight(self):
        # 对打多轮，谁的血量先小于等于0，谁就输了
        while True:
            self.my_hp = self.my_hp - self.your_power*2
            self.your_hp = self.your_hp - self.my_power*2
            if self.my_hp<=0:
                # pycharm 快捷键， ctrl+D 可以复制当前行
                print("我的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("我的剩余血量为",self.my_hp)
                print("你的剩余血量为",self.your_hp)
                print("你输了")
                break

game = Game()
game.fight()

