# 下述程序从键盘读入多个以逗号分隔的元素并将其组织在一个列表中，然后遍历列表删除其中重复的元素。具体地，假设列表中存在k个值为a的元素，删除前k-1个元素，保留最后一个，不同元素在列表中的相对位置不应被改变。
#
# v = list(eval(input()))
# print("before:",v)
#
# for x in v:
#     cnt = v.count(x)
#     if cnt >= 2:
#         for i in range(cnt-1):
#             v.remove(x)
#
# print("after:",v)
# 上述程序的运行结果为（第一行为测试输入）：
#
# 4, 3, 2, 3, 2, 4, True
# before: [4, 3, 2, 3, 2, 4, True]
# after: [3, 3, 2, 4, True]
# 对照上述执行结果的第2行及第3行，显然程序的执行结果不符合设定目标。原列表中的3保留了两个！
#
#
# 【错误分析】
#
# 程序在遍历循环（第4行）的内部执行了移除列表元素的操作（第8行）。一边遍历列表一边修改列表甚至删除列表元素可能使得遍历发生混乱，产生意料之外的结果。
#
#
#
# 请修改上述程序，使其可以正常工作。
#
# 输入格式:
# 由逗号分隔的多个值
#
# 输出格式:
# 参考输出样例，注意不同元素在列表中的相对位置不应被改变
#
# 输入样例:
# 4, 3, 2, 3, 2, 4, True
# 输出样例:
# before: [4, 3, 2, 3, 2, 4, True]
# after: [3, 2, 4, True]
#
# 请接着往下看：你的程序真的对了吗？
# 多数读者的解题思路是制造一个v列表的复制品以避免在遍历v的同时删除v中的元素。该解决方案可以通过本题设置的全部测试。但这并不意味着该解决方案是“完全正确”的。请尝试下述输入：
#
# 1,7,6,7,7,True,'a',9.8,'a',True
#
# 很遗憾，程序将产生错误的输出：
# before: [1, 7, 6, 7, 7, True, 'a', 9.8, 'a', True]
# after: [6, 7, 9.8, 'a', True]
# 产生这种意外结果的原因是：在Python里1和True是相等的！ 0和False也是相等的！ 在使用列表的count()函数，index()函数，remove()函数时，1和True, 0和False被不加区分地对待。
#
# 下述代码的执行结果证实了这一点：
#
# v = [1,True,2,True,0,False]
# print("count of 1:", v.count(1), ",count of True:", v.count(True))
# print("count of 0:", v.count(0), ",count of False:", v.count(False))
# print("index of True:",v.index(True), ",index of False",v.index(False))
# v.remove(True)
# print("after v.remove(True):",v)
# 其执行结果为：
#
# count of 1: 3 ,count of True: 3     #1,True都同时为1或True
# count of 0: 2 ,count of False: 2    #0,False都同时为0或False
# index of True: 0 ,index of False 4  #下标0的1被视为True
# after v.remove(True): [True, 2, True, 0, False]   #1被当作True移除了
#
# 解题思路： 请参考《Python编程基础及应用实验教程》。
# 该书是高等教育出版社《Python编程基础及应用》教材的配套实验指导书。
