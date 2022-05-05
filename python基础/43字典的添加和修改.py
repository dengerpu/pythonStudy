my_dict = {'name': 'itcast', 1: '我是1也是1.0'}
print(my_dict)
# 字典中添加和修改数据，使用key值进行添加和修改
# 字典[key] = 数据值，如果key值存在，就是修改，如果可以key值不存在，就是添加

my_dict['age'] = 18  # key值不存在，添加
print(my_dict)

my_dict['name'] = 'dengerpu'  # key值存在，修改
print(my_dict)

# 注意点key值int 的1 和float的1.0代表一个key值
print(my_dict[1])
print(my_dict[1.0])