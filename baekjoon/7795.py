
def eat(a,b):
    a.sort()
    b.sort()
    #print(a,b)

    count = 0

    count = 0
    #b에서 a보다 커지는 곳 찾아서 거기보다 앞쪽 개수
    for aVal in a:
        #print('aVal',aVal)
        res = 0
        start, end = 0, len(b)-1
        while start <= end:
            mid = (start + end) // 2
            if b[mid] < aVal:
                #print('----')
                res = mid+1
                start = mid + 1
            else:
                end = mid - 1
        #print(res)
        count += res

    return count



T = int(input())
while(T!=0):

    N,M = input().split()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = eat(A,B)
    print(count)

    T -= 1
