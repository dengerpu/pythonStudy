my_list = ['aaa', 'bbb', 'ccc', 'ddd']

# 向列表中添加数据的方法，都是直接在原列表中添加，不会返回新的列表
my_list.append('add')
print(my_list)

result = my_list.append(12)
print(result)  # None关键词，表示空

# 列表.insert(下标， 数据) 在指定的下标位置进行添加数据
my_list.insert(0,'hello')
print(my_list)
my_list.insert(3,'第三个')
print(my_list)

# 列表.extend（可迭代对象） # str 列表，会将可迭代对象中的数据逐个添加到原列表的末尾
my_list.extend('123')
print(my_list)  # ['hello', 'aaa', 'bbb', '第三个', 'ccc', 'ddd', 'add', 12, '1', '2', '3']
my_list.extend(['abc','edf'])
print(my_list)  # ['hello', 'aaa', 'bbb', '第三个', 'ccc', 'ddd', 'add', 12, '1', '2', '3', 'abc', 'edf']