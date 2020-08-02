"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
# 定义类，首字母大写
class Dog:
    # 属性——静态：毛色：白色，四条腿，一条尾巴
    color = "white"
    legs = 4
    tail = 1
    # 方法——动态：狗会叫、吃、跑、摇尾巴
    def bark(self):
        print("狗会发出汪汪的叫声")
    def eat(self):
        print("狗会吃火腿肠")
    def run(self):
        print("狗会跑步遛弯")
    def wag(self):
        print("狗会摇尾巴")
# 类的实例化
dog = Dog()
# 调用类的属性
print(f"狗的毛色是:",Dog.color)
print(f"狗有{Dog.legs}条腿")
print(f"狗有{Dog.tail}条尾巴")
# 调用类的方法
dog.bark()
dog.eat()
dog.run()
dog.wag()