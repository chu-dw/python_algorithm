student = 0

n,m = map(int,input().split())
graph = [[2] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

#테스트
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print( graph[i][j],' ', end='')
#     print('')

#플로이드 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1,n+1):
    count = 0
    for b in range(1,n+1):
        if graph[a][b] == 1 or graph[b][a] == 1:
            count = count + 1
            print('test',count)
    if count == n - 2:
        student = student + 1


print(student)