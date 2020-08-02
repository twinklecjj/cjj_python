# 导入模块——进行模块化改造
from python_practice.python_practice2.demo2.tonglao.tonglao import TongLao
# 定义一个XuZhu类，继承于童姥
class XuZhu(TongLao):
    # 定义一个read（念经）的方法
    def read(self):
        # 打印“罪过罪过”
        print("罪过罪过")
# 实例化类，并传参
xuzhu = XuZhu("无崖子",1000,100,1200,100)
# 调用类的方法
xuzhu.read()