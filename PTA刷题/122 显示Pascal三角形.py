# 输入行数n,显示n行Pascal三角形。数字间有一个空格。每行最后一个数字后有一个空格。
#
# 输入格式:
# 在一行中输入行数n。
#
# 输出格式:
# 输出n行Pascal三角形。
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 4
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 1
# 1 1
# 1 2 1
# 1 3 3 1
def Pascal(n):
    lst = []
    for i in range(n):
        for j in range(len(lst)-1):
            lst.append(lst.pop(0) + lst[0])
        lst.append(1)
    return lst


n = int(input())
pascla_list = []
for i in range(1, n+1):
    pascla_list.append(Pascal(i))

for i in range(n):
    for j in range(i+1):
        print(pascla_list[i][j], end=' ')
    print()