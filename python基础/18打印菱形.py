n = int(input('请输入行数：'))
i = 0
for i in range(n):
    k = 0
    for k in range(n-i-1):
        print(end=' ')
    j = 0
    for j in range (2*(i+1)-1):
        print('*',end='')
    print()
i = 0
for i in range (n-1):
    k = 0
    for k in range(i+1):
        print(end=' ')
    j = 0
    for j in range(2*(n-i-1)-1):
        print('*', end='')
    print()