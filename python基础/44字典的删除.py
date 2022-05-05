my_dict = {'name': 'dengerpu', 'age': 19, 1: 'float'}

# 根据key值删除数据 del 字典名【key】
del my_dict[1]
# del my_dict[12]  #  删除不存在的会报错
print(my_dict)

# 字典.pop（key） 根据key值删除，返回值是删除的key对应的value值
result = my_dict.pop('age')
print(result)
print(my_dict)

# 字典.clear（） 清空字典，删除所有的键值对
my_dict.clear()
print(my_dict)

# del 字典名   直接将这个字典删除了，不再使用这个字典
del my_dict  # 后面的代码不能再使用这个变量了