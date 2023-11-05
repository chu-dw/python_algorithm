in_tuple = str(input())
result = []

print(in_tuple)

s = in_tuple[2:-2]
print(s)

s = s.split('},{')
print(s)

s.sort(key=len)
print(s)

for i in s:
    temp = i.split(',')
    for j in temp:
        if int(j) not in result:
            result.append(int(j))

print(result)