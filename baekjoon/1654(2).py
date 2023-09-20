n,k = list(map(int,input().split()))

len = []

for i in range(n):
    len.append(int(input()))


print(len)

count = 1000000;


while True:
    count_val = 0
    print("while\n")
    print("count:", count)
    for j in range(n):
        line = (len[j] // count)
        print(line)
        count_val = count_val + line

    print("cv",count_val)
    count = count - 1
    if count_val == k:
        print(line)
        print("count:", count+1)
        exit()