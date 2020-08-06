# -*-coding:utf-8-*-
import json
# json.dump 表示把python对象写入在文件中
# json.dumps 表示把python对象 ,转化成字符串（dumps 代表dump-> string）
dict_hogwarts = {
    "a" : [1,2,3],
    "name": ["sprider man", "星矢"]
}
# 在data.json当中写入python object 数据
with open("data.json", "w") as f:
    json.dump(dict_hogwarts, f , ensure_ascii=False)
print(dict_hogwarts)
print(type(dict_hogwarts))
print(json.dumps(dict_hogwarts))
print(type(json.dumps(dict_hogwarts)))

json_load = json.load(open("data.json"))
print("使用json_load的数据为", json_load)
print("使用json_load的数据为", type(json_load))
# json_loads
data=json.dumps(dict_hogwarts)
json_loads = json.loads(data)
print("使用json_loads的数据为", json_loads)
print("使用json_loads的数据为", type(json_loads))