M,N = list(map(int,input().split()))
list = list(map(int,input().split()))

start, end = 1, 1000000000
result = 0

while start <= end:
    mid = (start+end)//2

    count = 0
    for i in list:
        count += i//mid

    if count >= M:
        #print('m', mid)
        result = max(result,mid)
        start = mid + 1

    else:
        end = mid - 1

    #print(mid)

print(result)



