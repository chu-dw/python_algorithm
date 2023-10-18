MAX = 2**31 - 1
N, K = map(int, input().split())
ml_list = []
for i in range(N):
    ml_list.append(input())

print(ml_list)

def check_loop(mid):
    for i in ml_list:
        i % K
        if (int(i) - i%K) - mid < 0:
            return 1
        else:
            return 0

start, end = 0, MAX
while start <= end:
    mid = (start + end) // 2
    chek = 0
    check = check_loop(mid)
    if check == 1:
        end = mid - 1
    elif check == 0:
        start = mid + 1
    print(mid)