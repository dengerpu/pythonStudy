"""
异常：在程序代码运行过程中遇到的错误，程序会报错，会终止代码的运行
异常捕获：是指在程序代码运行过程中，遇到的错误，不让程序代码终止，而让其急促运行，同时可以给使用者一个提示信息
并记录这个错误，便于后期改进

try:
    可能发生异常的代码
expect 异常的类型：
    发生异常执行的代码
"""

print('其他的代码...')
num = input('请输入一个数字')
# ZeroDivisionError: division by zero
try:
    num = 10 / int(num)
    print(f'计算结果是：{num}')
except ZeroDivisionError:
    print('输入有误')
print('其他代码执行...')

