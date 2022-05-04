# 有如下两行代码：
# tuple1 = (2)
# tuple2 = (2,)
# 请问tuple1与tuple2有什么不同
# tuple1 是int 类型 ，tuple2 是tuple类型
# 对于tuple1 = （2），python解释器会将小括号理解成一个运算符号，那么这时候 返回的值是一个int类型
# 所以对于只有一个元素的元组来说，要创建一个元组，那么就必须要加逗号


# 有如下代码，请回答问题？
my_tuple = ("itcast", "python", "CPP", 18, 3.14, True)
# 1.  使用下标的方法，输出元组中的元素 `"CPP"`
# 2.  使用 for 循环遍历元组
# 3.  使用 while 循环遍历元组
print(my_tuple[2])
for i in my_tuple:
    print(i)
print('*'*20)
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1