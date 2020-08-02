# 定义类，首字母大写
class SunWuKong:
    # 属性，身高：120cm、体重：80斤
    height = 120
    weight = 80
    # 方法——动态：筋斗云，七十二变，火眼金睛，打架
    def jdy(self):
        print("孙悟空常驾着筋斗云，一个筋斗能行十万八千里")
    def qseb(self):
        print("孙悟空的绝招是：七十二变")
    def hyjj(self):
        print("孙悟空有一双火眼金睛")
    def fight(self):
        print("孙悟空打架的武器是如意金箍棒")
# 类的实例化
sunwukong=SunWuKong()
# 调用类的属性
print(f"孙悟空的身高是:{sunwukong.height}cm")
print(f"孙悟空的体重是:{sunwukong.weight}斤")
# 调用类的方法
sunwukong.jdy()
sunwukong.qseb()
sunwukong.hyjj()
sunwukong.fight()