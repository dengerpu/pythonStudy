# 输入长度不超过80的英文文本，统计该文本中长度为n的单词总数（单词之间只有一个空格）。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。
# 每组数据首先输入1个正整数n（1≤n≤50），然后输入1行长度不超过80的英文文本（只含英文字母和空格）。注意：不要忘记在输入一行文本前吸收换行符。
#
# 输出格式:
# 对于每组测试数据，输出长度为n的单词总数。
#
# 输入样例:
# 2
# 5
# hello world
# 5
# acm is a hard game
# 输出样例:
# 2
# 0
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    word_list = input().split()
    for word in word_list:
        if len(word) == n:
            count += 1
    print(count)