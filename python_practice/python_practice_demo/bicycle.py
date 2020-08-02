"""
写一个Bicycle(自行车)类,有run(骑行)方法, 调用时显示骑行里程km(骑行里程为传入的数字):
再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume属性通过，参数传入,
同时有两个方法：
1. fill_charge(vol)用来充电, vol为电量
2. run(km)方法用于骑行,每骑行10km消耗电量1度,
当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
"""
# 定义Bicycle(自行车)类，首字母大写
class Bicycle:
    # 定义run(骑行)方法
    def run(self,km):
        # f:字面量插值传递km参数
        print(f"用脚一共骑行了{km}km，好累好累啊")
# 定义一个电动自行车类EBicycle继承自Bicycle,Bicycle是父类，EBicycle是子类
class EBicycle(Bicycle):
    # 注意2：第一种属性——类属性：类体内、方法之外
    # valume = 1000
    # 构造方法
    def __init__(self,valume):
        # 注意2：第二种属性——实例属性：类体内、方法内，并且以“self.变量名”的方式，去定义的变量
        # 定义电池电量valume属性，通过参数传入
        self.valume = valume
        # 注意2：第三种属性——普通属性：类体内、方法内，局部变量（我只在当前的方法内有用）
        # valume = valume
    # 定义fill_charge(vol)方法用来充电, vol为电量
    def fill_charge(self,vol):
        print(f"电动车已充电{vol}度")
        print(f"充完电后还有{vol+self.valume}度")
    #  定义run(km)方法用于骑行,每骑行10km消耗电量1度
    def run(self, km):
        # 有电的时候能骑到的最大公里数
        e_km=self.valume * 10
        print(f"电动自行车的最大公里数:{e_km}km")
        # 当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
        # 当用电能骑的公里数大于我们要骑的公里数
        if km - e_km <= 0:
            print(f"用电一共骑了{km}km")
        else:
            # 用脚骑的公里数=总公里数-用电的公里数
            print(f"用电一共骑了{e_km}km")
            # 注意3：调用父类的方法——super().子类的方法名
            # 第一种调用父类的方法：和普通实例化类调用方法相同
            # bike = Bicycle()
            # bike.run(km-e_km)
            # 第二种调用父类的方法：
            super().run(km-e_km)
            
    # pass占位符
    # pass

# 继承之后子类可以调用父类的属性和方法
# 注意1：构造函数的参数，需要在实例化类的时候传递
ebike = EBicycle(100)
# ebike.fill_charge(10)
# 注意4：当子类中有和父类重名的方法或者属性，那么首先选择的是子类的
ebike.run(10000)


# # 类在实例化的时候需要加括号
# # 用bike变量作为实例变量，去存放实例化后的实例对象
# bike =  Bicycle()
# # 调用run方法，并传参
# bike.run(1000)