# 小明购物之后搞不清最贵的物品价格和所有物品的平均价格，请帮他编写一个程序实现。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试先输入1个整数n（1≤n≤100），接下来的n行中每行输入1个英文字母表示的物品名及该物品的价格。测试数据保证最贵的物品只有1个。
#
# 输出格式:
# 对于每组测试，在一行上输出最贵的物品名和所有物品的平均价格，两者之间留一个空格，平均价格保留1位小数。
#
# 输入样例:
# 3
# a 1.8
# b 2.5
# c 1.5
# 输出样例:
# b 1.9
try:
    while True:
        n = int(input())
        shop_dict = {}
        for i in range(n):
            shop, price = input().split()
            shop_dict[shop] = float(price)
        max_price = max(shop_dict.values())
        for key, value in shop_dict.items():
            if value == max_price:
                print(key, end=' ')
        all_price = sum(shop_dict.values())
        aver = all_price / len(shop_dict)
        print('%.1f' % aver)
except EOFError:
    pass