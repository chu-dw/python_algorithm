# import sys
#
# f = sys.stdin.readline
# result = []
#
# n = int(f())
# num1, num2 = map(int, f().split())
# m = int(f())
#
# net = [[] for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, f().split())
#     net[a].append(b)
#     net[b].append(a)
#
# visited = [False]*(n+1)
#
# def dfs(v, count):
#     count += 1
#     visited[v] = True
#
#     if v == num2:
#         result.append(count)
#
#     for i in net[v]:
#         if not visited[i]:
#             dfs(i, count)
#
# dfs(num1,0)
#
# if len(result) == 0:
#     print(-1)
# else:
#     print(result[0]-1)

import sys

f = sys.stdin.readline
result = []

n = int(f())
num1, num2 = map(int, f().split())
net = [[]*(n+1) for _ in range(n+1)]
m = int(f())

for i in range(m):
    a, b = map(int, f().split())
    net[a].append(b)
    net[b].append(a)
#print(net)
visited = [False]*(n+1)

def dfs(v, count):
    count += 1
    visited[v] = True

    if v == num2:
        result.append(count)

    for now in net[v]:
        if not visited[now]:
            dfs(now, count)

dfs(num1, 0)


if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)