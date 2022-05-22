import math


class circle(object):
    def __init__(self, r):
        self.r = float(r)

    def perimeter(self):
        print(f'半径为{self.r}的圆，周长为{math.pi*2*self.r:.2f}')

    def area(self):
        print(f'半径为{self.r}的圆，面积为{math.pi*math.pow(self.r, 2):.2f}')


try:
    r = input('请输入半径：')
    circle = circle(r)
    circle.perimeter()
    circle.area()
except Exception as e:
    print(e)

