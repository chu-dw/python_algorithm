n = int(input())
card = list(input().split())
m = int(input())
findList = list(input().split())

#print(card, findList)
count = {}

for c in card:
    #print(c)
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
#print(count)

for f in findList:
    if f in count:
        result = count.get(f)
        print(result , end=' ')
    else:
        print(0 , end=' ')



