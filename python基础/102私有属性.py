'''
私有属性：在原属性名上加上两个下划线，即可
目的：保证数据的相对安全
想要访问和使用私有属性：定义一个公有的方法，通过这个方法使用
'''


class People(object):
    def __init__(self):
        # 在属性名的前边加上__类名前缀
        self.__icbc_money = 0

    def get_money(self):
        return self.__icbc_money

    def set_money(self, money):
        self.__icbc_money += money


xw = People()
# print(xw.__icbc_money)
# 实例对象.__dict__可以查看对象具有的属性信息，类型是字典。字典的key是属性名，value是属性值
print('赋值之前：', xw.__dict__)  # 赋值之前： {'_People__icbc_money': 0}
xw.__icbc_money = 1000 # 不是修改私有属性，而是添加了一个同名字的公有属性
print('赋值之后：', xw.__dict__)  # 赋值之后： {'_People__icbc_money': 0, '__icbc_money': 1000}
print(xw.__icbc_money)
print('='*20)
print(xw.get_money())
xw.set_money(200)
print(xw.get_money())
print( xw.__dict__)   # {'_People__icbc_money': 200, '__icbc_money': 1000}
xw._People__icbc_money = 10000  # bug可以直接修改私有属性的值
print(xw.get_money())
print( xw.__dict__)