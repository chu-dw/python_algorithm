n = int(input())

line = list(map(int, input().split()))
line2 = [11 for i in range(n)]


for i in range(n):

    left = line[i]
    print("left",left)

    print("i",i)

    for j in range(i+1):

        print("i j",i, j)

        lowerCount = 0
        for l in range(i+1):
            print("ll",l)
            if line2[l] < left:
                lowerCount += 1

        print("low",lowerCount)
        if lowerCount == 0:
            line2[left] = i + 1
            print("if", line2)
        else:
            line2[left + lowerCount+1] = i + 1
            print("else", line2)

        break

    #line2[left - lowerCount] = i

    print("test")


print(line)