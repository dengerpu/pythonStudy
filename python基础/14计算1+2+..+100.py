i = 1
result = 0
while i <= 100:
    result += i
    i += 1

print(result)

j = 1
result = 0
for j in range(1,101):
    result += j
print(result)

i = 2
result = 0
while i <= 100:
    result += i
    i += 2

print(result)

i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1

print(result)