"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
# 定义类，首字母大写
class TongLao:
    # 构造方法
    def __init__(self, name,my_hp,my_power,your_hp,your_power):
        # 实例属性：类体内、方法内，并且以“self.变量名”的方式，去定义的变量
        # 定义name属性，通过参数传人
        self.name = name
        # 定义属性——my_hp:我的血量，my_power:我的武力值，your_hp：你的血量，your_power:你的武力值（通过传入的参数得到）
        self.my_hp = my_hp
        self.my_power = my_power
        self.your_hp = your_hp
        self.your_power = your_power
    # 定义一个see_people方法
    def see_people(self):
        # if...elif...elif...语句判断，
        # 如果传入”WYZ”（无崖子），则打印，“师弟！！！！”
        if self.name == "无崖子":
            print("师弟！！！！")
        # 如果传入“李秋水”，打印“呸，贱人”
        elif self.name == "李秋水":
            print("呸，贱人")
        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif self.name == "丁春秋":
            print("叛徒！我杀了你")
    # 定义一个fight_zms方法（天山折梅手）
    def fight_zms(self):
        # 调用天山折梅手方法，将自己的武力值提升10倍，血量缩减2倍
        # 定义my_power1：提升10倍后我的武力值，my_hp1，缩减2倍后我的血量
        my_power1 = self.my_power * 10
        my_hp1 = self.my_hp / 2
        # 定义打斗一个回合后，我的剩余血量以及你的剩余血量
        self.my_final_hp = my_hp1 - self.your_power
        self.your_final_hp = self.your_hp - my_power1
        # 进行一回合制对打，打完之后，比较双方血量。血多的一方获胜
        # if...elif...else...语句判断
        #当我的剩余血量小于你的剩余血量时，打印双方的剩余血量并输出我输了，退出整个循环
        if self.my_final_hp < self.your_final_hp:
            # 输出你的剩余血量和我的剩余血量，并给出判断结果
            print("我的剩余的血量是：", self.my_final_hp)
            print("你的剩余的血量是：", self.your_final_hp)
            print("我输了")
            # 跳出所有循环
        # 当我的剩余血量大于你的剩余血量时，打印双方的剩余血量并输出你输了，退出整个循环
        elif self.my_final_hp > self.your_final_hp:
            # 输出我的剩余血量和你的剩余血量，并给出判断结果
            print("我的剩余的血量是：", self.my_final_hp)
            print("你的剩余的血量是：", self.your_final_hp)
            print("你输了")
            # 跳出所有循环
        else:
            # 当我的剩余血量等于你的剩余血量时，抛出一个异常
            raise Exception("no peace, 不要平局，战斗到最后一刻")
# 实例化类,并传参
tonglao = TongLao("无崖子",1000,100,1600,100)
# 调用类的方法
tonglao.see_people()
tonglao.fight_zms()






