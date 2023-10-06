n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

print(dp)  # (a,b) -> (a+1, b), (a+1, b+1)

for i in range(1,n):    #1층: 2개,  2층: 3개 / 2중 반복으로 dp 2층부터 순서대로 접근
    for j in range(i+1):
        if j == 0:       #왼쪽라인, 왼쪽위 존재x
            dp[i][j] = dp[i][j] + dp[i-1][j]
        elif j == i:      #오른쪽 라인, 오른쪽 위 존재x
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i-1][j-1])   #왼쪽 오른쪽중 큰값
    print(dp)

print(max(dp[n-1]))
