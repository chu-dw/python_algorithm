n, t = input().split()
n = int(n)
t = int(t)
answer = []
for i in range(n):
    n,s,c = map(int,input().split())

    bus_list = []

    for j in range(int(c)):
        bus_list.append(int(n))
        n = int(n) + int(s)

    #print(i, bus_list)

    start, end = 0, c-1
    while start <= end:
        mid = (start+end)//2
        if bus_list[mid] >= t:
            #print(bus_list[mid])
            end = mid-1
        elif bus_list[mid] < t:
            start = mid+1

    #print('end',bus_list[mid])
    wait = bus_list[mid] - t
    #print('wait',wait)
    answer.append(wait)


#print(answer)
result_val = min(answer)
if result_val < 0:
    result_val = -1
print(result_val)
