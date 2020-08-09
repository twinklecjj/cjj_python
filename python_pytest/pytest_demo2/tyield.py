# -*-coding:utf-8-*-
# yield 生成器  通过next()来获取生成器里面的下一个值
def provider():
    for i in range(0, 10):
        print("开始操作")
        # yield 没有打印值，默认输出none
        yield i  # 相当于return i，同时记录了上一次的执行位置
        print("结束操作")


# 定义生成器
p = provider()
# 打印生成器
print(p)
# print(next(p))只打印一次，不输出结束操作
# print(next(p))
# 第二次print(next(p))：从结束操作开始
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
for i in p:
    print(i)
