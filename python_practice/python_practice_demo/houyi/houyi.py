# 快捷键导入：alt+enter（回车）
# 文件名、路径名、变量名、函数名、类名，不要和python内置库冲突
from python_practice.python_practice_demo.game.game import Game

# 后裔继承角色的hp和power
class HouYi(Game):
   #  子类的init构造方法覆盖掉了父类的构造方法
   # 第一种
   # def __init__(self):
   # 第二种
   # def __init__(self, houyi_hp, your_hp):
   #  第三种
   def __init__(self,houyi_hp,your_hp,defense):
       # 继承父类的构造方法,并传参
       # 第一种
       # super().__init__(1000,1000)
       # 第二种
       # 使用关键字传参方式，给game父类传参
       super().__init__(my_hp=houyi_hp, your_hp=your_hp)
       # self.defense = 100
       # 第三种
       self.defense = defense

   # 定义一个fight方法
   def fight(self):
       # 对打多轮，谁的血量先小于等于0，谁就输了
       while True:
           # 定义打斗多个回合后，我的剩余血量以及你的剩余血量
           self.my_hp = self.my_hp + self.defense - self.your_power
           self.your_hp = self.your_hp - self.my_power
           # if...elif...语句判断
           # 当我的剩余血量<=0时，打印双方的剩余血量并输出我输了，退出整个循环
           if self.my_hp <= 0:
               # 输出你的剩余血量和我的剩余血量，并给出判断结果
               print("后裔的剩余的血量是：", self.my_hp)
               print("你的剩余的血量是：", self.your_hp)
               print("后裔输了")
               # 跳出所有循环
               break
           # 当你的剩余血量<=0时，打印双方的剩余血量并输出你输了，退出整个循环
           elif self.your_hp <= 0:
               # 输出我的剩余血量和你的剩余血量，并给出判断结果
               print("后裔的剩余的血量是：", self.my_hp)
               print("你的剩余的血量是：", self.your_hp)
               print("你输了")
               # 跳出所有循环
               break
# 第一种
# houyi = HouYi()
# 第二种
# houyi = HouYi(1000,1000)
# 第三种
houyi = HouYi(1000,1000,100)
houyi.fight()
