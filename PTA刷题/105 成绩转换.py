# 百分制成绩转换为五级计分制时，90分以上为A，80～89分为B，70～79分为C，60～69分为D，0～59分为E。请把输入的百分之成绩转换为五级计分制输出。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数score。
#
# 输出格式:
# 对于每组测试，在一行上输出百分制成绩score对应的字符等级。若score超出百分制范围，则输出“error!”。引号不必输出。
#
# 输入样例:
# 1
# 61
# 102
# 输出样例:
# E
# D
# error!
try:
    while True:
        score = int(input())
        if 90 <= score <= 100:
            print('A')
        elif 80 <= score <= 89:
            print('B')
        elif 70 <= score <= 79:
            print('C')
        elif 60 <= score <= 69:
            print('D')
        elif 0 <= score <= 59:
            print('E')
        else:
            print('error!')
except EOFError:
    pass