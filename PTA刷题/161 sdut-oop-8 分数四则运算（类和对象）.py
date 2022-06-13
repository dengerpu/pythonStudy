# 定义类Fraction，在其中定义属性:numerator和denominator，分别表示分子和分母。
#
# 然定再定义两个分数的加、减、乘、除运算的方法。
#
# 在主类中输入2个分数，计算它们的四则运算结果。
#
# 提示：若用Python语言来实现，不必自行创建类，可直接使用 fractions模块处理分数的表示与运算。
#
# 输入格式:
# 第一行是整数N，表示待进行分数四则运算式子的数量。接下来包含N行输入。
#
# 每行数据是一个字符串，格式是"a/boc/d"。
#
# 其中a, b, c, d为数字（每个数字保证在int类型范围内，为正数并且不存在正号）。o是运算符"+"或者"-","*",""。
#
# 输出格式:
# 对于每一行分数四则运算，输出一行计算结果。
#
# 注意：结果应符合书写习惯，没有多余的符号、分子、分母，并且化简至最简分数形式。
#
# 输入样例:
# 5
# 1/100+3/100
# 1/4-1/2
# 1/3-1/3
# 1/2*2/1
# 1/2\1/2
# 输出样例:
# 1/25
# -1/4
# 0
# 1
# 1
from fractions import Fraction

n = int(input())
for i in range(n):
    value = input()
    legth = len(value)
    count = 0
    for j in value:
        count += 1
        if j == '+':
            x = Fraction(value[:count-1])  # x是运算符前面的数
            y = Fraction(value[count:legth])  # y是运算符后面的数
            print(x + y)
            break
        elif j == '-':
            x = Fraction(value[:count-1])  # x是运算符前面的数
            y = Fraction(value[count:legth])  # y是运算符后面的数
            print(x - y)
            break
        elif j == '*':
            x = Fraction(value[:count-1])  # x是运算符前面的数
            y = Fraction(value[count:legth])  # y是运算符后面的数
            print(x * y)
            break
        elif j == '\\':  # 相当于\
            x = Fraction(value[:count - 1])  # x是运算符前面的数
            y = Fraction(value[count:legth])  # y是运算符后面的数
            print(x / y)
            break

# fractions模块下Fraction函数使用方法
# Fraction函数支持分数运算，输入参数可以是一对整数，一个分数，一个小数或者一个字符型数字。
#
# 1.化简
#
# 默认参数分子为0，分母为1。
# 输入两个整数(分别作为分子、分母)，返回两数约分后的结果。
# 注意：分母>=0
#
#  Fraction(2/4)
#  # 输出 1/2
# 1
# 2
# 2. 对于浮点数
#
# 输入浮点数，会返回该数的分子分母形式。
#
# Fraction(4.5)
# #输出 9/2
# 1
# 2
# Fraction(3)
# # 输出 3
# Fraction(3.0)
# # 输出 3
#
# 1
# 2
# 3
# 4
# 5
# 3.对于分数
#
# 输入分数，会返回该数的分子分母形式。
#
#  Fraction(3/2)
# #  输出 3/2
# 1
# 2
# 4.输入字符型数字，会返回该数的分子分母形式。
#
# Fraction('4.5')
# # 输出9/2
#  Fraction('9/2')
# # 输出 9/2
