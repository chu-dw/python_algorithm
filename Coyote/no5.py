n,m = map(int,input().split())

list = list(map(int, input().split(' ')))

ball = [0] * (m+1)

for i in list:
    ball[i] = ball[i]+1

print(ball)

result = 0
for i in range(1,m+1):
    n = n-ball[i]   #전체 볼리공 수에서 무게 i인 공 개수 빼줌
    result = result + (ball[i] * n)  #같은 무게 제거하고 나머지 경우 수

print(result)













