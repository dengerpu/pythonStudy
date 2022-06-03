# 信息安全很重要，特别是密码。给定一个5位的正整数n和一个长度为5的字母构成的字符串s，加密规则很简单，字符串s的每个字符变为它后面的第k个字符，其中k是n的每一个数位上的数字。第一个字符对应n的万位上的数字，最后一个字符对应n的个位上的数字。简单起见，s中的每个字符为ABCDE中的一个。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据在一行上输入非负的整数n和字符串s。
#
# 输出格式:
# 对于每组测试数据，在一行上输出加密后的字符串。
#
# 输入样例:
# 12345 ABCDE
# 输出样例:
# BDFHJ
try:
    while True:
        num, keyword = input().split()
        encypt = ''
        for i, j in zip(num, keyword):
            encypt += chr(ord(j)+int(i))
        print(encypt)
except EOFError:
    pass