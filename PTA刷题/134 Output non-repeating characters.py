# Enter a string, and then pick out the 10 left-most non-repeating characters (case-sensitive characters). If the number of non-repeating characters is less than 10, output the actual number of characters.
#
# Input Format:
# Output Format:
# Sample Inputs1:
# Hello world, hello python
# Sample Output1:
# Helo wrd,h
# Sample Inputs2:
# succeed
# Sample Output2:
# suced
word = input()
lst = []
for i in word:
    if i not in lst:
        lst.append(i)
if len(lst) >= 10:
    lst = lst[0:10]
    print(''.join(lst))
else:
    print(''.join(lst))