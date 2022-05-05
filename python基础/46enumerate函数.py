# enumerate（）函数用于将一个可遍历的数据对象组合成一个索引序列，
# 同时列出数据和数据下标，一般用在for循环当中
my_list = ['a', 'b', 'c', 'd', 'e']
for i in my_list:
    print(my_list.index(i), i)
print('*'*30)

# enumerate可以将可迭代序列中元素所在的下标和具体元素组合在一起，变成元组
for j in enumerate(my_list):
    print(j)
print(type(enumerate(my_list)))  # <class 'enumerate'>