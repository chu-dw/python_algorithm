n,m = list(map(int,input().split(' ')))

s = []


def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


def dfs2(pre):
    if len(s)==m:
        print(' '.join(map(str, s)))
        return

    for i in range(1,n+1):
        if (i not in s) and (i>pre):
            s.append(i)
            dfs(i)
            s.pop()


dfs(1)
print('\n')
dfs2(0)