# 定义类，首字母大写
class ZhangJie:
    # 属性，身高：180cm、体重：130斤，年龄:37岁
    height = 180
    weight = 130
    age = 37
    # 方法——动态：唱歌，吃
    def sing(self):
        print("张杰会唱歌，是一位歌手")
    def eat(self):
        print("张杰爱吃土豆烧排骨")
# 类的实例化
zhangjie = ZhangJie()
# 调用类的属性
print(f"张杰的身高是:{zhangjie.height}cm")
print(f"张杰的体重是:{zhangjie.weight}斤")
print(f"张杰的年龄是:{zhangjie.age}岁")
# 调用类的方法
zhangjie.sing()
zhangjie.eat()
