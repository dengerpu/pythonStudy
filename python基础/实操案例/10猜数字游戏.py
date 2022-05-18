import random
value = random.randint(1, 100)
i = 0
while True:
    try:
        num = int(input('请输入你要猜的数字：'))
    except Exception:
        print('输入有误，请重新输入')
    else:
        if(num < value):
            print('小了')
        elif(num > value):
            print('大了')
        else:
            # print('恭喜你猜对了')
            break
        i += 1
print(f'恭喜你猜对了，共用了{i}次，数字是{value}')


