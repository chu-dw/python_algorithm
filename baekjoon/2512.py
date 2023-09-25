n = int(input())
req_list = list(map(int, input().split()))
m = int(input())


start, end = 0, max(req_list)
while(start<=end):
    mid = (start+end)//2
    total = 0
    for i in req_list:
        if i > mid:
            total += mid  #상한선 보다 크면 상한액
        else:
            total += i  #상한선 보다 작으니 요청값

    if total <= m: #총합 더 작으니 상한선 올림
        start = mid+1
    else:  #총합 더 크니 상한선 내림
        end = mid-1

print(end)