# 鸡兔同笼问题，从键盘读取脚数，头数，输出鸡数和兔数。
#
# 输入格式:
# 脚数
#
# 头数
#
# 输出格式:
# 鸡数
#
# 兔数
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 94
# 35
# 输出样例:
# 23
# 12
# foot = int(input())
# head = int(input())
# # 设鸡x条，兔y条
# # 2*x + 4*y = foot
# # x + y = head
# # 先自己手动算： x=head-y  2*(head-y) + 4*y = foot
# # 2*y = foot - 2*head
# y = int((foot - 2*head)/2)
# x = head - y
# print(x)
# print(y)
foot = int(input())
head = int(input())
for x in range(0, head+1):
    if 2*x + 4*(head-x) == foot:
        print(x)
        print(head-x)
        break