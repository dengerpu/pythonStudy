# 百鸡问题：“今有鸡翁一，值钱五；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，问鸡翁母雏各几何。”
#
# 百鸡问题是北魏数学家张丘建在《张丘建算经》中提出的一个世界著名的不定方程问题，它给出了由三个未知量的两个方程组成的不定方程组的解。
#
# 自张丘建以后，中国数学家对百鸡问题的研究不断深入，百鸡问题也几乎成了不定方程的代名词，从宋代到清代围绕百鸡问题的数学研究取得了很好的成就。
#
# 《张丘建算经》约成书于公元466—485年间，共三卷93题，包括测量、纺织、交换、纳税、冶炼、土木工程、利息等各方面的计算问题。其体例为问答式，条理精密，文词古雅，是中国古代数学史上的杰作，也是世界数学资料库中的一份宝贵的遗产。后世学者北周甄鸾、唐李淳风相继为该书做了注释。特别是唐代，经太史令李淳风注释整理，收入《算经十书》，成为当时算学馆先生的必读书目。《张丘建算经》现传本有92问，比较突出的成就有最大公约数与最小公倍数的计算，各种等差数列问题的解决、某些不定方程问题求解等。
#
# （以上文字摘自百度百科）
#
# 百钱百鸡问题的白话版：100元钱买100只鸡，公鸡5元1只，母鸡3元1只，小鸡1元3只。问公鸡、母鸡、小鸡各多少只（某种鸡可以为0只）？
#
# 百钱百鸡的结果如输出样例所示。
#
# 现在把100改为n，即n元钱买n只鸡，各种鸡价格不变，结果又如何呢？
#
# 输入格式:
# 测试数据有多组，处理到文件尾。每组测试输入一个整数n（100<=n<=1000）。
#
# 输出格式:
# 对于每组测试，按公鸡、母鸡、小鸡的数量（按公鸡数从小到大的顺序）逐行输出各种买法（每行数据之间空一个空格）。
#
# 输入样例:
# 100
# 输出样例:
# 0 25 75
# 4 18 78
# 8 11 81
# 12 4 84
try:
    while True:
        n = int(input())
        for x in range(int(n/5)+1):
            for y in range(int(n/3)+1):
                if 5 * x + y * 3 + (n-x-y)/3 == n:
                    print(x, y, n-x-y)
except EOFError:
    pass