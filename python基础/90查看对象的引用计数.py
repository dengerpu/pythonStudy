import sys


class Dog(object):
    def __del__(self):
        print('程序结束执行，或者引用计数为0执行...')


dog = Dog()  # 1
print(sys.getrefcount(dog))  # 2,显示的时候会比实际多1
dog2 = dog
print(sys.getrefcount(dog))  # 3
del dog
print(sys.getrefcount(dog2))  # 2
del dog2