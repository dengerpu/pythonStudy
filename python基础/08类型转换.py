num = 1
num1 = float(num)
print(type(num1))  # <class 'float'>
print(num1)

num4 = float("3.14")
num5 = float("10")
print(type(num4))
print(type(num5))

# price = input('请输入苹果价格')
# weight = input('请输入重量')
# result = float(price)*float(weight)
#
# print(f"苹果单价为{price}元/斤，购买了{weight}斤，需要支付{result}元")

# 类型转化，将原始数据转换为我们需要的数据类型，在这个过程中，不会改变原始的数据，会生成一个新的数据
pi = 3.14
num = int(pi)
print(type(pi))
print(type(num))

my_str = '10'
num1 = int(my_str)
print(type(num1))

# eval()还原原来的数据类型，去掉字符串的引号
num6 = eval('100')
num7 = eval('3.14')
print(type(num6))  # <class 'int'>
print(type(num7))  # <class 'float'>

num8 = eval('num7')  # num7 是已经定义好的变量，可以使用不会报错
print(num8)

num9 = eval('hello')  # 报错，hello变量没有定义，不能使用
print(num9)