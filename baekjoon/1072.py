x, y = map(int,input().split())

#print(x,y)
win = (y*100)//x
#print(win)

if win >= 99:
    print(-1)

else:
    answer = 0
    start = 1
    end = x   #처음 주어진 만큼 더 이기면 무조건 바뀐다..?

    while start <= end:
        mid = (start+end)//2
        if ((y+mid)*100 // (x+mid)) <= win:
            start = mid+1
        else:
            answer = mid
            end = mid-1
        #print('t', answer)

    print(answer)