# 定义类，首字母大写
class XieNa:
    # 属性，身高：166cm、体重：92斤，年龄:39岁
    height = 166
    weight = 92
    age = 39
    # 方法——动态：唱歌，主持，表演
    def sing(self):
        print("谢娜会唱歌，是一位歌手")
    def zc(self):
        print("谢娜会主持，是一位主持人")
    def act(self):
        print("谢娜会表演，是一位演员")
# 类的实例化
xiena = XieNa()
# 调用类的属性
print(f"谢娜的身高是:{xiena.height}cm")
print(f"谢娜的体重是:{xiena.weight}斤")
print(f"谢娜的年龄是:{xiena.age}岁")
# 调用类的方法
xiena.sing()
xiena.zc()
xiena.act()