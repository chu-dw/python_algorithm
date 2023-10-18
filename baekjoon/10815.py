N = int(input())
list1 = list(map(int,input().split()))
M = int(input())
list2 = list(map(int,input().split()))

answer = [0]*M
index = 0

list1.sort()

for num in list2:
    #print('n',num)

    start, end = 0, len(list1)-1
    while start <= end:
        mid = (start + end) // 2
        if num == list1[mid]:
            #print(1)
            answer[index] = 1
            break
        elif num < list1[mid]:
            end = mid-1
        elif num > list1[mid]:
            start = mid+1
    index += 1

print(*answer, sep=' ')
