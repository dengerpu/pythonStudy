"""
try:
    可能发生异常的代码
except (异常的类型1，异常类型2，...)：
    发生异常执行的代码
"""

print('其他的代码...')
num = input('请输入一个数字')
# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'm'
try:
    num = 10 / int(num)
    print(f'计算结果是：{num}')
except (ZeroDivisionError, ValueError) as e:
    print('输入有误', e)
print('其他代码执行...')

"""
try:
    可能发生异常的代码
except 异常的类型1：
    发生异常类型1，执行的代码
except 异常的类型2：
    发生异常类型2，执行的代码
except ...：
    ....
"""

# print('其他的代码...')
# num = input('请输入一个数字')
# # ZeroDivisionError: division by zero
# # ValueError: invalid literal for int() with base 10: 'm'
# try:
#     num = 10 / int(num)
#     print(f'计算结果是：{num}')
# except ZeroDivisionError as e:
#     print('0不能做除数', e)
# except ValueError as e:
#     print('不能输入字母或汉子', e)
# print('其他代码执行...')