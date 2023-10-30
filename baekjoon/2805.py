N, M = map(int,input().split())
tree = list(map(int,input().split()))

def cut(trees, height):
    count = 0
    for tree in trees:
        if tree > height:
            count += (tree - height)
    return count

start, end = 0, 2000000000

while(start<=end):
    mid = (start+end)//2
    height = cut(tree,mid)
    print(height)
    if height >= M:
        start = mid + 1
        print(mid)
    elif height < M:
        end = mid - 1
        print(mid)
        res = mid

print('result',res)