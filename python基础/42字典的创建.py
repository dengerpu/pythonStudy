# 字典 dict 定义使用{} 定义，是由键值对组成（key:value）
# 变量 = {key1：value1，key2：value2}，一个key:value键值对是一个元素
# 字典的key 可以是字符串类型和数字类型（int float） 不能是列表
# value值可以是任何类型

# 1.定义空字典
my_dict = {}
my_dict1 = dict()
print(my_dict, type(my_dict))  # {} <class 'dict'>
print(my_dict1, type(my_dict1))  # {} <class 'dict'>

# 2.定义带数据的字典
my_dict2 = {'name': 'zahngsan', 1: '123', 2.0: '2.0', 'abc': ['a','b','c']}
print(my_dict2)

# 3.访问value值，在字典中没有下标的概念，使用key值访问对应的value
print(my_dict2['name'])
print(my_dict2['abc'][0])
print(my_dict2.get(2.0))

# 如果key值不存在
# print(my_dict2['gender'])  # KeyError: 'gender'

# 字典.get(key),如果key值不存在，不会报错，返回的是None
print(my_dict2.get('gender'))  # None
# 字典.get(key,value) 如果key存在，返回key对应的value值，如果key不存在，返回书写的数据值
print(my_dict2.get(1,'123'))
print(my_dict2.get(3,'456'))  # key值不存在，返回456

print(len(my_dict2))  # 计算的是key的多少