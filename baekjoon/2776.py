def binary_search(note1, note2):

    return_val = []

    for n2 in note2:
        start, end = 0, len(note1)-1
        flag = False

        while start <= end:
            mid = (start+end)//2
            if n2 == note1[mid]:
                return_val.append(1)
                flag = True
                break
            elif n2 < note1[mid]:
                end = mid-1
            elif n2 >= note1[mid]:
                start = mid+1
        if flag == False:
            return_val.append(0)

    return return_val


ouput = []

t = int(input())

for i in range(t):
    n = int(input())
    note1_in = list(input().split())
    m = int(input())
    note2_in = list(input().split())

    note1_in.sort()
    ouput += binary_search(note1_in, note2_in)


for i in ouput:
    print(i)