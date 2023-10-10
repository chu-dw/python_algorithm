import sys

#입력 input 말고 공부 -> input 시간 초과

N, M = input().split()
rank = [sys.stdin.readline().split() for _ in range(int(N))]
result = []

#print(rank)



def binary(rank, cnt):
    res = 0
    start, end = 0, len(rank)-1
    while start <= end:
        mid = (start+end)//2
        if int(rank[mid][1]) >= cnt:
            end = mid - 1
            res = mid
        elif int(rank[mid][1]) < cnt:
            start = mid + 1
    return res

for i in range(int(M)):
    cnt = int(sys.stdin.readline())
    #print(int(cnt))
    print(rank[binary(rank, int(cnt))][0])
