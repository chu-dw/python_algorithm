import sys
from collections import deque

f = sys.stdin.readline

n, m = map(int,f().split())
graph = []

for i in range(n):
    graph.append(list(map(int,f().split())))

print(graph)

val = []

def bfs(x,y):
    dx = [0, 1, 0,-1]
    dy = [1, 0,-1, 0]
    cnt = 1

    queue = deque()
    queue.append((x,y,cnt))
    graph[y][x] = 0
    print('xy',x,y, queue)

    while queue:
        x,y,cnt = queue.popleft()
        print('xy2',x,y,cnt)

        for i in range(4):
            x_t = x + dx[i]
            y_t = y + dy[i]
            print(x_t,y_t)

            if 0 <= x_t < n and 0 <= y_t < m:
                if graph[y_t][x_t] == 1:
                    print(graph)
                    print(cnt)
                    queue.append((x_t, y_t, cnt+1))
                    graph[y_t][x_t]=0

    print(cnt)
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:

            returnVal = bfs(i,j)
            val.append(returnVal)

print('val',val)