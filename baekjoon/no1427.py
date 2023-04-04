array = []
array = list(map(int, str(input())))

array.sort(reverse=True)

for i in array:
    print(i, end='')