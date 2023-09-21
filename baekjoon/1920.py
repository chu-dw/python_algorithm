n = int(input())
list1 = list(input().split())
m = input()
find = list(input().split())

list1.sort()

for num in find:
    start, end = 0, n - 1
    findCheck = False

    while start<=end:

        mid = (start + end) // 2

        if num == list1[mid]:
            print(1)
            findCheck = True
            break
        elif num >= list1[mid]:
            start = mid+1
        elif num < list1[mid]:
            end = mid-1

    if findCheck == False:
        print(0)





