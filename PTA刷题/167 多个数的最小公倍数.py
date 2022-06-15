# 两个整数公有的倍数称为它们的公倍数，其中最小的一个正整数称为它们两个的最小公倍数。当然，n个数也可以有最小公倍数，例如：5，7，15的最小公倍数是105。
# 输入n个数，请计算它们的最小公倍数。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试先输入一个整数n（2≤n≤20），再输入n个正整数（属于[1，100000]范围内）。这里保证最终的结果在int型范围内。
#
# 输出格式:
# 对于每组测试，输出n个整数的最小公倍数。
#
# 输入样例:
# 3
# 3 5 7 15
# 5 1 2 4 3 5
# 8 7 15 12 3 4 6 4 9
# 输出样例:
# 105
# 60
# # 1260两个整数公有的倍数称为它们的公倍数，其中最小的一个正整数称为它们两个的最小公倍数。当然，n个数也可以有最小公倍数，例如：5，7，15的最小公倍数是105。
# 输入n个数，请计算它们的最小公倍数。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组测试先输入一个整数n（2≤n≤20），再输入n个正整数（属于[1，100000]范围内）。这里保证最终的结果在int型范围内。
#
# 输出格式:
# 对于每组测试，输出n个整数的最小公倍数。
#
# 输入样例:
# 3
# 3 5 7 15
# 5 1 2 4 3 5
# 8 7 15 12 3 4 6 4 9
# 输出样例:
# 105
# 60
# # 1260
#
# fd = eval(input('请输入要研究的多个整数，以逗号隔开：\n'))
# fdx = list()  # 各整数的所有因子，以列表存于此列表中。
# for fi in fd:
#     print(fi, "= ", end="")
#     fid = list()  # 每个整数因式分解后各因子存放于此
#     if fi == 1 or fi == 2:
#         fid.append(fi)  # 1或2，特殊处理
#     x = 2
#     while x <= int(fi ** 0.5):
#         if fi % x != 0:
#             x += 1
#         if fi % x == 0:
#             fid.append(str(x))
#             fi = int(fi / x)
#     fid.append(str(fi))
#     fid.sort()
#     fdx.append(fid)
#     print("*".join(fid))  # 打印因式分解
#
# fdd = [i for d in fdx for i in d]  # 所有整数的因子汇总。
# fdd = list(set(fdd))  # fdd中含有所有的因子，注意每个因子只出现一次。
#
# minks = list()  # 求最小公倍数。各因子以在各整数中出现的最大次数出现于此。
# maxks = list()  # 求最大公约数。各共有因子以在各整数中同时出现的最小次数出现于此。
#
# for x in fdd:
#     x_c = list()  # 各整数中含x因子的个数，汇总于此。注意，此中可能含有0.
#     for d in fdx:
#         x_c.append(d.count(x))
#     for i in range(max(x_c)):
#         minks.append(x)
#     if min(x_c) != 0:
#         for j in range(min(x_c)):
#             maxks.append(x)
#
# mink = 1
# for i in minks:
#     i = int(i)
#     mink *= i  # 这就是最小公倍数
# minks.sort()
# fmink = "= " + "*".join(minks)
# print("最小公倍数为{:^8}".format(mink))
# print(mink, fmink)
#
# maxk = 1
# for i in maxks:
#     i = int(i)
#     maxk *= i  # 这就是最大公约数
# maxks.sort()
# fmaxk = "= " + "*".join(maxks)
# print("最大公约数为{:^4}".format(maxk))
# if len(maxks) > 1:
#     print(maxk, fmaxk)
#
# print("验算如下：")
# for fi in fd:
#     print(mink, "= ", fi, "*", int(mink / fi))
# for fi in fd:
#     print(fi, "/", maxk, "= ", int(fi / maxk), )


def Least_common_multiple(a, b):  # 求最小公倍数
    max_num = max(a, b)
    for i in range(max_num, a*b+1):
        if i % a == 0 and i % b == 0:
            return i


t = int(input())
for i in range(t):
    n, *lst = map(int, input().split())
    lst2 = list(set(lst))  # 这种方式去重后顺序会变
    lst2.sort(key=lst.index)  # 这样可以保证顺序不变，对于此题顺序变不变无所谓
    while len(lst2) != 1:  # 和最小生成树原理很相似
        a = lst2.pop()
        b = lst2.pop()
        c = Least_common_multiple(a, b)
        lst2.append(c)

    print(lst2[0])

