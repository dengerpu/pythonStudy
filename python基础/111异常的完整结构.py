"""
try:
    可能发生异常的代码
except Exception as e:
    发生异常执行的代码
    print(e)
else:
    代码没有发生异常，会执行
finally:
    不管有没有发生异常，都会执行
"""
try:
   num = input('请输入数字')
   num = 10 / int(num)
   print(num)
except Exception as e:
    print(e)
else:
    print('代码没有发生异常，会执行...')
finally:
    print('不管代码发没发生异常，一定会执行...')
print('其他的代码...')