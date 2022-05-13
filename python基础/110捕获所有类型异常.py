print('其他的代码...')
num = input('请输入一个数字')
try:
    num = 10 / int(num)
    print(f'计算结果是：{num}')
except Exception as e:
    print('输入有误', e)
print('其他代码执行...')