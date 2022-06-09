# 设计一个三维向量类，实现向量加法、减法以及向量与标量的乘法和除法运算。后面添加下面代码完成：
#
# 捕获.JPG
#
# 输入样例:
#
# 输出样例:
# (4, 6, 8)
# (4, 6, 8)
# (-2, -2, -2)
# (3, 6, 9)
# (1.5, 2.0, 2.5)
# (1, 2, 2)
class Vecter(object):
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def __add__(self, other):
        result = Vecter()
        result.X = self.X + other.X
        result.Y = self.Y + other.Y
        result.Z = self.Z + other.Z
        return result

    def add(self, other):
        result = Vecter()
        result.X = self.X + other.X
        result.Y = self.Y + other.Y
        result.Z = self.Z + other.Z
        return result

    def __sub__(self, other):
        result = Vecter()
        result.X = self.X - other.X
        result.Y = self.Y - other.Y
        result.Z = self.Z - other.Z
        return result

    def __mul__(self, other):
        result = Vecter()
        result.X = self.X * other
        result.Y = self.Y * other
        result.Z = self.Z * other
        return result

    def __truediv__(self, other):
        result = Vecter()
        result.X = self.X / other
        result.Y = self.Y / other
        result.Z = self.Z / other
        return result

    def __floordiv__(self, other):
        result = Vecter()
        result.X = self.X // other
        result.Y = self.Y // other
        result.Z = self.Z // other
        return result

    def show(self):
        my_triple = (self.X, self.Y, self.Z)
        print(my_triple)


v1 = Vecter(1, 2, 3)
v2 = Vecter(3, 4, 5)
v3 = v1+v2
v3.show()
v3 = v1.add(v2)
v3.show()
v4 = v1-v2
v4.show()
v5 = v1*3
v5.show()
v6 = v2/2
v6.show()
v7 = v2//2
v7.show()
