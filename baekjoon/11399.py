n = int(input())
line = list(map(int, input().split()))

line.sort()
# print(line)

time = 0
total = 0
index = 1
for i in range(n):
    while index <= n:
        # print("index",index)
        time = time + line[index-1]
        index += 1
        # print("time",time)
        total = total + time

print(total)

