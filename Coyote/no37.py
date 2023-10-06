INF = int(1e9)

n = int(input())
m = int(input())

table = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            table[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < table[a][b]:
        table[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            table[a][b] = min(table[a][b], table[a][k] + table[k][b])


for a in range(1, n+1):
    for b in range(1, n+1):
        if table[a][b] == INF:
            print("INF", end="")
        else:
            print(table[a][b], end="  ")
    print()