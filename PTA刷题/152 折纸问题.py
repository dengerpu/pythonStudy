# 一张纸厚0.2mm, 问至少对折多少次后，纸的厚度超过珠穆朗玛峰（8848m)
#
# 输出格式:
# 折叠次数=26
# 折叠后厚度=13421.77
#
# 输入样例:
#
# 输出样例:
# 在这里给出相应的输出。例如：
#
# 折叠次数=26
# 折叠后厚度=13421.77
height = 0.0002
count = 0
while True:
    if height > 8848:
        break
    height = 2*height
    count += 1
print(f'折叠次数={count}')
print(f'折叠后厚度={height:.2f}')
