print('其他功能代码...')
num = input('请输入数字：')
try:
    try:
        a = int(num)    # 输入字母，会发生ValueError。内层try代码中发生的异常，没有被捕获，会向外层传递
    except ZeroDivisionError:
        print('发生异常...')
    finally:
        print('我都执行了....')
    num = 10 / a
    print(f'计算的结果：{num}')
except Exception as e:
    print(e)

print('其他的代码...')