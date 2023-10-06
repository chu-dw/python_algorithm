n = int(input())

a = list(map(int,input().split()))

def binary_s(array, start, end):
    while start <= end:
        mid = (start + end) // 2   # mid = index값

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else: # array[mid] < mid
            start = mid + 1
    return None

array = binary_s(a,0,n-1)
if array == None:
    print(-1)
else:
    print(array)

