# 定义类QiaoFeng，首字母大写
class QiaoFeng:
    # 属性，身高：185、体重：200
    height=185
    weight=200
    # 方法
    def fight_xlsbz(self):
        print("乔峰的绝招是：降龙十八掌")
    def video(self):
        print("乔峰出场自带bgm")
# 类的实例化
qiaofeng=QiaoFeng()
print(f"乔峰的身高是:{qiaofeng.height}cm")
print(f"乔峰的体重是:{qiaofeng.weight}斤")
qiaofeng.fight_xlsbz()
qiaofeng.video()