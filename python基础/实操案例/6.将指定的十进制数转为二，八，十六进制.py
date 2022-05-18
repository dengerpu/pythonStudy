def fun():
    num = int(input('请输入一个十进制数：'))
    print(num, '的二进制数为：', bin(num))  # 第一种写法，使用了个数可变的位置参数
    print(str(num)+'的二进制数为：'+bin(num))  # 第二种写法，使用+作为连接符，+左右均为str
    print('%s的二进制数为：%s' % (num, bin(num)))  # 第三种写法，格式化字符串
    print('{0}的二进制位数为：{1}'.format(num, bin(num)))  # 第三种写法，格式化字符串
    print(f'{num}的二进制位数为：{bin(num)}')  #  第三种方式，格式化字符串
    print('-'*30)
    print(f'{num}的八进制数为：{oct(num)}')
    print(f'{num}的十六进制数为：{hex(num)}')


while True:
    try:
        fun()
        break
    except:
        print('输入有误...')
