# 现需要统计若干段文字(英文)中的不同单词数量。
# 如果不同的单词数量不超过10个，则将所有单词输出(按字母顺序)，否则输出前10个单词。
#
# 注1：单词之间以空格(1个或多个空格)为间隔。
# 注2：忽略空行或者空格行。
# 注3：单词大小写敏感，即'word'与'WORD'是两个不同的单词 。
#
# 输入说明
# 若干行英文，最后以!!!!!为结束。
#
# 输出说明
# 不同单词数量。
# 然后输出前10个单词（按字母顺序），如果所有单词不超过10个，则将所有的单词输出。
#
# 输入样例
# Failure is probably the fortification in your pole
# It is like a peek your wallet as the thief when you
# are thinking how to spend several hard-won lepta
# when you Are wondering whether new money it has laid
# background Because of you, then at the heart of the
# most lax alert and most low awareness and left it
# godsend failed
# !!!!!
# 输出样例
# 49
# Are
# Because
# Failure
# It
# a
# alert
# and
# are
# as
# at
# 代码长度限制
# 16 KB
# 时间限制
# 400 ms
# 内存限制
# 64 MB
# count = 0
# lst = []
# while True:
#     s = input()
#     if s == "!!!!!":
#         break
#     my_str = s.strip()  # 去除两边的空格和换行
#     my_set = set(my_str.split())  # 以空格分隔字符，使用set可以自动去重
#     for item in my_set:
#         if item not in lst:  # 去除列表中重复的数据
#             count += 1
#             lst.append(item)
#
# lst.sort()
# print(count)
# if count <= 10:
#     for i in lst:
#         print(lst[i])
# else:
#     for i in range(10):
#         print(lst[i])
# 上面这个写法存在非零返回



count = 0
ls = []
while True:
    s = input()
    if s == "!!!!!":
        break
    a = s.split()
    for item in a:             #删除列表重复冗余
        if item not in ls:
            count = count + 1
            ls.append(item)
ls.sort()           #列表排序
print(count)
if count <= 10:
    for i in range(count):
        print(ls[i])
else:
    for i in range(10):
        print(ls[i])







