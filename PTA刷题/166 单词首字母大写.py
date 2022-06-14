# 输入一个英文句子，要求将每个单词的首字母改成大写字母。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一行，包含一个长度不超过100的英文句子（仅包含大小写英文字母和空格），单词之间以一个空格间隔。
#
# 输出格式:
# 对于每组测试，输出按照要求改写后的英文句子。
#
# 输入样例:
# I like acm
# i want to get accepted
# 输出样例:
# I Like Acm
# I Want To Get Accepted
def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


try:
    while True:
        words_list = input().split()
        words_list = [word.title() for word in words_list]  # 首字母大写
        print_list(words_list)
except EOFError:
    pass
