N, K = map(int,input().split())
mak = []
for i in range(N):
    val = int(input())
    mak.append(val)


#print(mak)
result = 0

start, end = 0, (2**31)-1
while start <= end:
    mid = (start+end)//2
    temp = 0
    for m in mak:
        temp += m//mid
    if temp >= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
