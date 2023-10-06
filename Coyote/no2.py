
array = input()
print(array)

result = 0

num = int(array[0])
result = num

for i in range(1, len(array)):
    if int(array[i-1]) <= 1:
        result = result + int(array[i])
    elif int(array[i-1]) > 1:
        result = result * int(array[i])

print(result)