my_list = [1, 3.14, 'dengerpu', False]

# index()   根据数据值，查找元素所在的下标，找到返回元素的下标，没有找到程序报错
# 列表中没有find方法，只有index() 方法
num = my_list.index(3.14)
print(num)  # 1

# num1 = my_list.index(100)  # 找不到程序会报错  ValueError: 100 is not in list

# count() 统计出现的次数
num3 = my_list.count(1)  # True也代表1
print(num3)

# in / not in  判断是否存在，存在是True ,不存在是False ,一般和if结合使用
num4 = 3.14 in my_list
print(num4)  # True

num4 = 3.14 not in my_list
print(num4)  # Falsre
