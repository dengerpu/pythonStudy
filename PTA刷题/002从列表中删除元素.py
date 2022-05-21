# 删除列表中所有符合条件的值。
#
# 输入格式:
# 输入n，代表要测试n次。每次测试：
# 首先，输入1行字符串（字符串内的元素使用空格分隔）
# 然后，输入要删除的元素x。
#
# 输出格式:
# 输出删除元素x后的每行字符串。如果元素全部被删除，则输出空行。
# 注意：行尾不得有多余的空格。
#
# 输入样例:
# 5
# 1 1 1 2 1 2 1 1 1
# 1
# 1 1 1 2 2 2 1 1 1
# 2
# ab ab ab cd cd de de
# ab
# 1 1 1 1
# 1
# x y x x x z
# t
# 输出样例:
# 2 2
# 1 1 1 1 1 1
# cd cd de de
#
# x y x x x z
# 注意：第2个样例输入，文件非常大，需考虑到效率，属于计算机专业学生需要考虑的问题。非专业的学生做不出来，不必太过纠结。
n = int(input())
for i in range(n):
    my_str = input()
    ch = input()
    my_list = list(my_str.split())
    c = []
    for item in my_list:
        if ch != item:
            c.append(item)
        else:
            continue
    print(' '.join(c))