schools_name = [['北京大学', '清华大学'],
               ['南开大学', '天津大学', '天津师范大学'],
               ['山东大学', '中国海洋大学']]
print(schools_name[1])  # ['南开大学', '天津大学', '天津师范大学']
print(schools_name[1][0])  # 南开大学
print(schools_name[1][0][0]) # 南

print('*'*30)
for schools in schools_name:
    for name in schools:
        print(name)