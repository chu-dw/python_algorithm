N, t = input().split()
N = int(N)
t = int(t)
answer = []
for i in range(N):
    n,s,c = map(int,input().split())

    bus_list = []

    for j in range(int(c)):
        bus_list.append(int(n))
        n = int(n) + int(s)

    #print(i, bus_list)

    check=0
    start, end = 0, c-1
    while start <= end:
        mid = (start+end)//2
        if bus_list[mid] >= t:
            #print('test',bus_list[mid])
            check = mid
            end = mid-1
        elif bus_list[mid] < t:
            start = mid+1

    #print('end',bus_list[check])
    wait = bus_list[check] - t
    #print('wait',wait)
    answer.append(wait)


#print('answer',answer)
result_val = min(answer)
if result_val < 0:
    result_val = -1
print(result_val)
