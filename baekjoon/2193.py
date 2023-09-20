n = int(input())

count = 1
val = 0

for i in range(n):
    count = count * 2
count = count-1


for j in range(count):
    bin = format(j,'b')
    #print(bin)

    if ('11' not in bin) and (len(bin)>=n):
        #print("답",bin)
        val = val+1

print(val)

