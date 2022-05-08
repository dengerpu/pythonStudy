# 递归形成的条件
# 1.函数自己调用自己
# 2.函数必须有一个终止条件
def get_age(n):
    if n==1:
        return 18
    else:
        return get_age(n-1)+2


print(get_age(1))
print(get_age(4))