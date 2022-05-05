my_dict = {'name': 'dengerpu', 'age': 18, 'gender': '男'}

# for循环体直接遍历字典，遍历字典的key值
for key in my_dict:
    print(key,my_dict[key])
print('='*30)

# 字典.keys() 获取字典中所有的key值，得到的类型是dict_keys,该类型具有的特点是
# 1. 可以使用list() 进行类型转换，即将其转换为列表类型
# 2. 可以使用for循环遍历
result = my_dict.keys()
print(result, type(result))  # dict_keys(['name', 'age', 'gender']) <class 'dict_keys'>
for key in result:
    print(key, my_dict[key])

result1 = list(result)
print(result1)

print('='*30)
# 字典.values() 获取所有的value值，类型为dict_values
# 1. 可以使用list()进行强制类型转换，
# 2. 可以使用for循环进行遍历
result = my_dict.values()
print(result, type(result))  # dict_values(['dengerpu', 18, '男']) <class 'dict_values'>
for value in result:
    print(value)

print('='*30)
# 字典.items() 获取所有的键值对，类型是dict_items，key,value组成元组类型
# 1. 可以使用list()进行强制类型转换
# 2.  可以使用for循环进行遍历
result = my_dict.items()
print(result, type(result))  # dict_items([('name', 'dengerpu'), ('age', 18), ('gender', '男')]) <class 'dict_items'>
for k, v in my_dict.items():
    print(k, v)
