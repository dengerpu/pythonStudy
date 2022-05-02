# 设计"过7 游戏” 程序,即在 1- 99 之间的数字中,如果数字 包含 7 或者是 7 的倍数,则输出"过...", 否则输出 具体的数字.
# i = 1
# while i < 100:
#     if (i % 7 == 0) or (i // 10 == 7 ) or (i % 10 == 7):
#         print('过')
#     else:
#         print(i)
#     i += 1

# for i in range (1, 100):
#     if (i % 7 == 0) or (i // 10 == 7 ) or (i % 10 == 7):
#         print('过')
#     else:
#         print(i)

# 编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入
# i = 3
# sys_username = 'python'
# sys_password = '123456'
# while i > 0:
#     user = input('请输入用户名：')
#     password = input('请输入密码：')
#     if (user == sys_username) and (password == sys_password):
#         print('欢迎光临')
#         break
#     else:
#         i -= 1
#         if i != 0:
#             print('账号或密码错误。您还有%d次机会' % i)
#         else:
#             print('你已输入错误次数超过三次，账户已被锁定')

# 猜数字游戏：电脑产生（1-100）的随机数，用户进行猜测，直到猜中为止。
# 1. 如果猜中，输出：恭喜你猜中了，数字是 xx。
# 2. 如果猜的数字大，输出：猜测的数字太大了，继续加油
# 3. 如果猜测的数字小，输出：猜测的数字有点小，再来一次
# import random
# print('猜数字游戏开始')
# sys_num = random.randint(1, 101)
# while True:
#     num = int(input('请输入数字：'))
#     if num == sys_num:
#         print('恭喜你猜中了，数字是 %d。' % sys_num)
#         break
#     elif num < sys_num:
#         print('猜测的数字有点小，再来一次')
#     else:
#         print('猜测的数字太大了，继续加油')

# 猜数字游戏：电脑产生（1-100）的随机数，用户进行猜测。
# 1. 如果猜中，输出：恭喜你猜中了，数字是 xx，猜测了xx次。
# 2. 如果猜的数字大，输出：猜测的数字太大了，继续加油
# 3. 如果猜测的数字小，输出：猜测的数字有点小，再来一次
# 4. 如果猜测5 次，还没有猜测出来，输出：太弱了,测试5次还没猜出来,不和你玩了
# import random
# sys_num = random.randint(1, 101)
# i = 0
# while True:
#     num = int(input('请输入数字'))
#     i += 1
#     if i < 5:
#         if num == sys_num:
#             print('恭喜你猜中了，数字是 %d，猜测了%d次' %(sys_num, i))
#             break
#         elif num < sys_num:
#             print('猜测的数字有点小，再来一次')
#         else:
#             print('猜测的数字太大了，继续加油')
#     else:
#         print('太弱了,测试5次还没猜出来,不和你玩了.数字是%d' % sys_num)
#         break

# import random

# # 电脑产生随机数
# num = random.randint(1, 100)
# # 记录用户输入的次数
# count = 0
#
# while count < 5:
#     # 提示让用户输入
#     my_num = int(input("请输入1-100之间的整数:"))
#     count += 1
#     if my_num == num:
#         print("恭喜你猜中了，数字是%d, 猜测了%d次" % (num, count))
#         break
#     elif my_num > num:
#         print("猜测的数字太大了，继续加油")
#         continue  # 本代码中可以不写
#     else:
#         print("猜测的数字有点小，再来一次")
# else:
#     print("太弱了,猜测5次还没猜出来,不和你玩了")

# 请用户输入一个数，使用while计算是否为素数(素数只能被 1 和本身整除)
# num = int(input('请输入数字：'))
# if num == 1 or num == 0:
#     print("%d 不是素数也不是合数" % num )
# else:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             print(f'{num}不是素数')
#             break
#         i += 1
#     if i == num:
#         print('%d是素数' % num)

# 要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。
my_str = input('请输入字符串')
for i in my_str:
    if i == 'p':
        break
    elif i == ' ':
        continue
    else:
        print(i)

