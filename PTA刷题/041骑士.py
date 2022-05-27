# 在国际象棋中，棋盘的行编号为1~8，列编号为a~h；马以“日”方式行走，根据马在当前棋盘上的位置，请问可以有几种合适的走法。如下图所示，设马（以H表示）在e4位置，则下一步可以走的位置是棋盘中粗体数字标注的8个位置：
#
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据输入一个字符（a~h）和一个整数（1~8），表示马所在的当前位置。
#
# 输出格式:
# 对于每组测试，输出共有几种走法。
#
# 输入样例:
# 1
# e4
# 输出样例:
# 8
n = int(input())
m = 8
for i in range(n):
    column, row = input()
    row = int(row)
    count = 0
    if m - row >= 2 and ord(column) - ord('a') >= 2:
        count += 2
    if m - row >= 2 and ord(column) - ord('a') == 1:
        count += 1
    if m - row >= 2 and ord('h') - ord(column) >= 2:
        count += 2
    if m - row >= 2 and ord('h') - ord(column) == 1:
        count += 1
    if m - row == 1 and ord(column) - ord('a') >= 2:
        count += 1
    if m - row == 1 and ord('h') - ord(column) >= 2:
        count += 1
    if row - 1 >= 2 and ord(column) - ord('a') >= 2:
        count += 2
    if row - 1 >= 2 and ord(column) - ord('a') == 1:
        count += 1
    if row - 1 >= 2 and ord('h') - ord(column) >= 2:
        count += 2
    if row - 1 >= 2 and ord('h') - ord(column) == 1:
        count += 1
    if row - 1 == 1 and ord(column) - ord('a') >= 2:
        count += 1
    if row - 1 == 1 and ord('h') - ord(column) >= 2:
        count += 1
    print(count)


