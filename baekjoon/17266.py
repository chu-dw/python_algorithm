N = int(input())
M = int(input())
lights = list(map(int,input().split()))

#print(lights)
last, height = lights[0],lights[0]

for i in range(1,len(lights)):
    temp = abs(last-lights[i])  # lights[0] - lights[1]
    # temp 는 둘사이 거리
    if temp % 2 == 0:
        temp = temp//2
    else:
        temp = (temp//2)+1

    height = max(height, temp)

    last = lights[i]

height = max(height, abs(N-lights[len(lights)-1]))

print(height)