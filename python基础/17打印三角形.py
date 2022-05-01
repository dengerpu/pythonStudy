n = int(input('请输入行数:'))
i = 0
for i in range(n):
    j = 0
    for j in range(i+1):
        print('*',end=' ')
    print()

print('-------------')
i = 0
for i in range(n):
    j = 0
    for j in range (n-i-1):
        print(end=' ')
    k = 0
    for k in range (i+1):
        print('*',end=' ')
    print()
