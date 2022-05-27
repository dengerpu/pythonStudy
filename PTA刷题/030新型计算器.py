# 题目：设计一个计算器，实现一个三维向量的加法，减法以及向量和标量的乘法和除法运算
# 提示：
# 1、定义类名为 VecCal，设计构造函数创建三维向量对象： def __init__(self, x=0,y=0,z=0) 用x,y,z指代三个维度的值
#
# 2、重写加法（+），减法（-），乘法（* ）和整除除法（//）运算，实现向量的加减乘除
#
# 3、除法运算作异常处理，当输入标量数字是0时，除法结果为 （0，0，0）
#
# 加法示例：
#
# def __add__(self, n):  # 加法
#     result = VecCal()  # 定义结果变量，也是一个三维向量，通过构造函数创建
#     result.X = self.X + n.X
#     result.Y = self.Y + n.Y
#     result.Z = self.Z + n.Z
#     return result         # 返回 执行加法运算后的向量结果
# 输入格式:
# 第一行输入一个三维向量，逗号分隔，如：1，2，3
#
# 第二行输入另一个三维向量，逗号分隔：如：4，5，6
#
# 第三行输入一个数字， 如：3
#
# 输出格式:
# (1, 2, 3) + (4, 5, 6) = (5, 7, 9)
#
# (1, 2, 3) - (4, 5, 6) = (-3, -3, -3)
#
# (1, 2, 3) * 3 = (3, 6, 9)
#
# (1, 2, 3) / 3 = (0, 0, 1)
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 1,2,3
# 4,5,6
# 3
# 输出样例:
# 在这里给出相应的输出。例如：
#
# (1, 2, 3) + (4, 5, 6) = (5, 7, 9)
# (1, 2, 3) - (4, 5, 6) = (-3, -3, -3)
# (1, 2, 3) * 3 = (3, 6, 9)
# (1, 2, 3) / 3 = (0, 0, 1)
class VecCal(object):
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def __add__(self, n):
        result = VecCal()
        result.X = self.X + n.X
        result.Y = self.Y + n.Y
        result.Z = self.Z + n.Z
        return result

    def __sub__(self, n):
        result = VecCal()
        result.X = self.X - n.X
        result.Y = self.Y - n.Y
        result.Z = self.Z - n.Z
        return result

    def __mul__(self, n):
        result = VecCal()
        result.X = self.X * n
        result.Y = self.Y * n
        result.Z = self.Z * n
        return result

    def __truediv__(self, n):
        result = VecCal()
        result.X = self.X // n
        result.Y = self.Y // n
        result.Z = self.Z // n
        return result

    def show(self):
        my_tuple = (self.X, self.Y, self.Z)
        return my_tuple


a, b, c = list(map(int, input().split(',')))
x, y, z = list(map(int, input().split(',')))
n = int(input())
v1 = VecCal(a, b, c)
v2 = VecCal(x, y, z)
print(f'{v1.show()} + {v2.show()} = {(v1 + v2).show()}')
print(f'{v1.show()} - {v2.show()} = {(v1 - v2).show()}')
print(f'{v1.show()} * {n} = {(v1 * n).show()}')
if n != 0:
    print(f'{v1.show()} / {n} = {(v1 / n).show()}')  # 其实n为0，可以输出为（0,0,0）
else:
    print(f'{v1.show()} / {n} = {(0, 0, 0)}')
