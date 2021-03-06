# 假设n是一个正整数，它的值不超过1000000，请编写一个程序，将n分解为若干个素数的乘积。
#
# 输入格式:
# 首先输入一个正整数T，表示测试数据的组数，然后是T组测试数据。每组测试数据输入一个正整数n（1< n ≤1000000）。
#
# 输出格式:
# 每组测试对应一行输出，输出n的素数乘积表示式，式中的素数从小到大排列，两个素数之间用一个“*”表示乘法。若输入的是素数，则直接输出该数。
#
# 输入样例:
# 2
# 9828
# 88883
# 输出样例:
# 2*2*3*3*3*7*13
# 88883
import math


def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end='*')
        else:
            print(lst[i])


def is_sushu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


# lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
#        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
#        113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
#        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
#        251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
#        317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
#        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
#        463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
#        557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
#        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
#        701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
#        787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
#        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
#        953, 967, 971, 977, 983, 991, 997]
# t = int(input())
# for i in range(t):
#     n = int(input())
#     if is_sushu(n):
#        print(n)
#     else:
#         result = n
#         k = 0
#         yin_lst = []
#         while result and k < len(lst):
#             if result % lst[k] == 0:
#                 yin_lst.append(lst[k])
#                 result = int(result / lst[k])
#             else:
#                 k += 1
#         print_list(yin_lst)

t = int(input())
for i in range(t):
    n = int(input())
    if is_sushu(n):
       print(n)
    else:
        x = 2
        yin_list = []
        while x <= int(n**0.5):
            if n % x != 0:
                x += 1
            else:
                yin_list.append(x)
                n = int(n/x)
        yin_list.append(n)
        print_list(yin_list)

