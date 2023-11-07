S, C = map(int,input().split())
pa = []
for i in range(S):
    pa.append(int(input()))

start, end = 0, 1000000
result = 0

while start<=end:
    mid = (start+end)//2

    temp = 0
    for i in pa:
        if mid == 0:
            temp = 0
        else:
            temp += i//mid

    #print('m',mid)
    #print('t = ',temp)
    if temp >= C:
        start = mid + 1
        result = mid

    else:
        end = mid - 1

#print(result)

pa_sum = 0
cnt = 0
if result == 0:
    pa_sum = 0
else:
    pa_sum = sum(pa) - (result * C)


print(pa_sum)


# 1 10
# 10
#
# 답 : 0

# 3 5
# 10
# 10
# 10
#
# 답 : 5

# 3 5
# 100
# 100
# 100
#
# 답 : 50