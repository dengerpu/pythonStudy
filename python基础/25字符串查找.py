my_str = 'hello world itcast and itcastcpp'

# find() 在字符串中查找是否存在某个字符串
# my_str.find(sub_str, start, end)
# sub_start ：要在字符串中查找的内容，类型str
# start:开始的位置，从哪里开始查找，默认是0
# end：结束的位置，查找到哪里结束，默认是len()
# 返回值，即方法执行的结果是什么，如果找到sub_str,则返回sub_str在my_str中的位置正数下标
# 如果没有找到，返回-1

print(my_str.find('hello'))  # 0
# 从下标为3的位置，开始查找字符串hello
print(my_str.find('hello', 3))  # -1

print(my_str.find('itcast'))
print(my_str.find('itcast',13))
# rfind() right find()  从右边开始查找
print(my_str.rfind('itcast'))

# index() 在字符串中查找是否存在某个字符串
# my_str.index(sub_str, start, end)
# sub_start ：要在字符串中查找的内容，类型str
# start:开始的位置，从哪里开始查找，默认是0
# end：结束的位置，查找到哪里结束，默认是len()
# 返回值，即方法执行的结果是什么，如果找到sub_str,则返回sub_str在my_str中的位置正数下标
# 如果没有找到，会报错
print(my_str.index('hello'))
print(my_str.index('itcast', 0))
print(my_str.index('itcast', 13, len(my_str)-1))
# print(my_str.index('aaa'))  # 找不到会报错
print(my_str.rindex('itcast'))

#   count(sub_str,start, end)统计出现的次数
print(my_str.count('hello'))
print(my_str.count('itcast'))
print(my_str.count('itcast', 13))
print(my_str.count('aaa'))
