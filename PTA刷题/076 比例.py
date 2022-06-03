# 某班同学在操场上排好队，请确定男、女同学的比例。
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试数据输入一个以“.”结束的字符串，串中每个字符可能是“MmFf”中的一个，“m”或“M”表示男生，“f”或“F”表示女生。
#
# 输出格式:
# 对于每组测试数据，在一行上输出男、女生的百分比，结果四舍五入到1位小数。输出形式参照### 输出样例:。
#
# 输入样例:
# FFfm.
# MfF.
# 输出样例:
# 25.0 75.0
# 33.3 66.7
try:
    while True:
        value = input().split('.')[0]
        man = value.count('m') + value.count('M')
        women = value.count('f') + value.count('F')
        print(f'{man/(man+women)*100:.1f} {women/(man+women)*100:.1f}')
except EOFError:
    pass