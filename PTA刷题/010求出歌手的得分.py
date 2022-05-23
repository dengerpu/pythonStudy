# 输入一个正整数n (n>4)，再输入n个实数，求出歌手的得分（保留2位小数）。设一歌唱评奖晚会上有n(n>4)个评委为歌手打分.评分规则:每个评委依次打分,再去掉2个最高分和2个最低分,计算余下的分数平均值为歌手的得分.
#
# 输入格式:
# 在第一行中输入n
# 在第二行中输入n个分数
#
# 输出格式:
# 在一行中输出平均分数
#
# 输入样例:
# 在这里给出一组输入。例如：
#
# 10
# 10 10 9 9 9 8 8 8 7 7
# 输出样例:
# 在这里给出相应的输出。例如：
#
# aver=8.50
n = int(input())
score_str = input()   # 这样输入真的没问题吗？我感觉有问题，这样输入上面的n就没价值了
score_list = score_str.split()
score_list = [float(x) for x in score_list]  # 转换成字符串
score_list.sort()
score_list = score_list[2:len(score_list)-2]  # 去掉两个最高分和最低分
result = 0
for i in score_list:
    result += i
aver = result / (n-4)
print(f'aver={aver:.2f}')
