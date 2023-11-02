N,M = map(int,input().split())
list = []
for i in range(M):
    val = int(input())
    list.append(val)

start, end = 0, 300000
res = 0

while start <= end:
    mid = (start+end) // 2
    print('m',mid)
    temp = 0
    for l in list:
        temp += l // mid
    print(temp)

    if temp <= N:
        start = mid + 1
        res = mid
    else:
        end = mid - 1


    print('r',res)