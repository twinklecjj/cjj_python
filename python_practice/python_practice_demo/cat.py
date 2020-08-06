# 定义类，首字母需要大写
class Cat:
    # 毛色，橘色， 四条腿
    # 会吃， 会叫， 会睡
    # 属性——静态
    color = "orange"
    leg = 4
    # 方法——动态，在类的方法中，是使用def关键字定义
    # def定义的 在类外叫做函数function, 在类内，叫做method
    def eat(self):
        print("猫会吃")
    def cry(self):
        print("猫会叫")
    def sleep(self):
        print("猫会睡")
print(Cat.color)
# 类的实例化,定义一个变量去存储类的实例化对象
cat=Cat()
# 变量调用类
cat.eat()
cat.cry()
cat.sleep()

