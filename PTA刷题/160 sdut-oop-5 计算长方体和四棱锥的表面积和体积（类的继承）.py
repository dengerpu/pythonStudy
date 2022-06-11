# 计算如下立体图形的表面积和体积。
#
# 008.jpg
#
# 从图中观察，可抽取长方体和四棱锥两种立体图形的共同属性到父类Rect中：长度：l 宽度：h 高度：z。
#
# 编程要求：
#
# （1）在父类Rect中，定义求底面周长的方法length( )和底面积的方法area( )。
#
# （2）定义父类Rect的子类立方体类Cubic，计算立方体的表面积和体积。其中表面积area( )重写父类的方法。
#
# （3）定义父类Rect的子类四棱锥类Pyramid，计算四棱锥的表面积和体积。其中表面积area( )重写父类的方法。
#
# （4）在主程序中，输入立体图形的长(l)、宽(h)、高(z)数据，分别输出长方体的表面积、体积、四棱锥的表面积和体积。
#
# 提示：
#
# （1）四棱锥体积公式：V=
# 3
# 1
# ​
#  Sh，S——底面积 h——高
#
# （2）在Java中，利用Math.sqrt(a)方法可以求得a的平方根（方法的参数及返回结果均为double数据类型）
#
# （3）在Python中，利用math模块的sqrt(a)方法，求得a的平方根。
#
# 输入格式:
# 输入多行数值型数据（double）；
#
# 每行三个数值，分别表示l、h、z，数值之间用空格分隔。
#
# 若输入数据中有0或负数，则不表示任何图形，表面积和体积均为0。
#
# 输出格式:
# 行数与输入相对应，数值为长方体表面积 长方体体积 四棱锥表面积 四棱锥体积（中间有一个空格作为间隔，数值保留两位小数）。
#
# 输入样例:
# 1 2 3
# 0 2 3
# -1 2 3
# 3 4 5
# 输出样例:
# 22.00 6.00 11.25 2.00
# 0.00 0.00 0.00 0.00
# 0.00 0.00 0.00 0.00
# 94.00 60.00 49.04 20.00
import math


class Rect(object):
    def __init__(self, l ,h, z):
        self.l = l
        self.h = h
        self.z = z

    def length(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return 2*(self.l + self.h)

    def area(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return self.l * self.h


class Cubic(Rect):
    def area(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return 2*self.h*self.l + 2*self.h*self.z + 2*self.l*self.z

    def volume(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return self.l*self.h*self.z


class Pyramid(Rect):
    def area(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return self.l*math.sqrt(self.z**2+((1/2)*self.h)**2) + self.h*math.sqrt(self.z**2+(1/2*self.l)**2) + self.l*self.h

    def volume(self):
        if self.h <= 0 or self.l <= 0 or self.z <= 0:
            return 0
        else:
            return (1/3)*self.l * self.h * self.z


while True:
    try:
        a, b, c = map(float, input().split())
        cubic = Cubic(a, b, c)
        pyramid = Pyramid(a, b, c)
        print(f'{cubic.area():.2f} {cubic.volume():.2f} {pyramid.area():.2f} {pyramid.volume():.2f}')
    except:
        break