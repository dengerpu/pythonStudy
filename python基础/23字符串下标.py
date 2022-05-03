# 下标也称为是索引，是一个整形数字，可以使正数也可以是负数
# 正数下标是从0开始的，表示第一个字符，-1标识最后一个字符
my_str = 'hello'
print(my_str[0])    # h
print(my_str[1])    # e
print(my_str[-1])   # o
print(my_str[-2])   # l

# len() 函数可以得到字符串的长度
print(len(my_str))
# 使用正数下标书写字符串中最后一个元素
print(my_str[len(my_str)-1])