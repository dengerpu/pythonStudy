list_sig = ['①', '②', '③', '④']
list_name = ['a', 'b', 'c', 'd']
for i in range(4):
    print(list_sig[i], list_name[i])

my_dict = {'①': 'a', '②': 'b', '③': 'c', '④': 'd'}
print('-'*30)
for k, v in my_dict.items():
    print(k, v)
print('-'*30)
for i in my_dict:
    print(i, my_dict[i])
print('-'*30)
for i in my_dict.values():
    print(i)
print('-'*30)
for k, v in zip(list_sig, list_name):
    print(k, v)
