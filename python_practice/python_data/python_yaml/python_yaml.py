import yaml

yaml_data = yaml.safe_load(open("data.yml"))
print(yaml_data)

a = [[{'a': 1}, 'admin2'], 'admin3']
# 方法一
# print(yaml.safe_dump(a))
# 方法二
with open("data3", "w") as f:
    yaml.safe_dump(a,f)