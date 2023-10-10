N, M = input().split()
char_dic = {}
charPower = []
result = []

for i in range(int(N)):
    title, power = input().split()
    char_dic[title] = int(power)

for i in range(int(M)):
    c = input()
    charPower.append(int(c))

#print(char_dic)
#print(charPower)
temp = 0

for i in char_dic.keys():

    start, end = 0,int(M)-1
    while start <= end:
        mid = (start+end)//2
        if charPower[mid] <= char_dic[i]:
            start = mid+1

        elif charPower[mid] > char_dic[i]:
            end = mid-1

    #print(start)

    for j in range(start-temp):
        print(i)
    temp = start

