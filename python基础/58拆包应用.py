#  交换两个变量的值
a = 10
b = 20

# 方法一
c = a
a = b
b = c
print(a, b)

# 方法二
a = a+b
b = a-b
a = a-b
print(a, b)

# 方法三 python中的使用，闭包和组包
a, b = b, a
print(a, b)