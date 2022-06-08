# Remove duplicate values from a list， the relative position of different elements in the list should not be changed.
#
# input format:
# output format:
# input sample:
# [4,7,5,6,8,6,9,5]
# output sample:
# 4 7 5 6 8 9
# Tip: The strings "[1,3,5]" can be converted to a list using the eval() function.
num_list = eval(input())
lst =[]
for i in num_list:
    if i not in lst:
        lst.append(i)
for i in range(len(lst)):
    if i != len(lst)-1:
        print(lst[i], end=' ')
    else:
        print(lst[i])