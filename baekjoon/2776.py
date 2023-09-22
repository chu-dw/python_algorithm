t = input()
n = int(input())
note1 = list(input().split())
m = input()
note2 = list(input().split())

for n1 in note1:
    start, end = n

    while start <= end:
        mid = (start+end) // 2

        if n1 == note2[mid]:
            print(1)
            break
        elif n1 < note2[mid]:
            end = mid-1
        elif n1 > note2[mid]:
            start = mid+1
