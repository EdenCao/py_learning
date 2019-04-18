dict_obj = {}
dict_obj["one"] = "1 - 菜鸟工具"
dict_obj[2] = "2 - 菜鸟工具"

tinydict = { "name": "runoob", "code": 1, "site": "www.runoob.com"}

print(dict_obj["one"])
print(dict_obj[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

tuple_build_dict = dict([("Runoob", 1), ("Google", 2), ("Taobao", 3)])
for_build_dict = {x: x ** 2 for x in (2, 4, 6)}
equal_build_dict = dict(Runoob = 1, Google = 2, Taobao = 3)
