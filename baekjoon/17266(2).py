

def bs(li, m):

    if li[1] - li[0] > m:
        return 0
    if li[-1] - li[-2] > m:
        return 0

    for i in range(1,len(li)-2):
        if (li[i+1] - li[i]) // 2 > m:
            return 0
    return 1

N = int(input())
M = int(input())
lights = list(map(int,input().split()))

start, end = 0,N

while start <= end:
    mid = (start+end) // 2
    if bs(lights, mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1


print(answer)