# 定义类，首字母大写
class HeJiong:
    # 属性，身高：172cm、体重：100斤，年龄:46岁
    height = 1742
    weight = 100
    age = 46
    # 方法——动态：唱歌，主持，写作，导演，表演
    def sing(self):
        print("何炅会唱歌，是一位歌手")
    def zc(self):
        print("何炅会主持，是一位主持人")
    def write(self):
        print("何炅会写作，是一位作家")
    def direct(self):
        print("何炅会导演，是一位导演")
    def act(self):
        print("何炅会表演，是一位演员")
# 类的实例化
hejiong=HeJiong()
# 调用类的属性
print(f"何炅的身高是:{hejiong.height}cm")
print(f"何炅的体重是:{hejiong.weight}斤")
print(f"何炅的年龄是:{hejiong.age}岁")
# 调用类的方法
hejiong.sing()
hejiong.zc()
hejiong.write()
hejiong.direct()
hejiong.act()