n,k = list(map(int,input().split()))

len = []
for i in range(n):
    len.append(int(input()))



start = 1
end = max(len)

while start <= end:
    mid = (start+end)//2
    count = [(i//mid) for i in len]
    #print(count)
    #print(sum(count))

    if sum(count) >= k:
        start = mid+1
    elif sum(count) < k:
        end = mid-1

print(end)
