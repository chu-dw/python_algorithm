n = int(input())
k = int(input())


way = 'e'

def boundary(i,j):
    if i<0 or i>=n or j<0 or j>=n:
        print('끝')
        return True

def left(i,j, way):

    if way == 'e':
        i=i-1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'n'
        return way

    elif way == 'w':
        i=i+1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 's'
        return way

    elif way == 'n':
        j=j-1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'w'
        return way

    elif way == 's':
        j=j+1
        if boundary(i, j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'e'
        return way


def right(i,j, way):

    if way == 'e':
        i=i+1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'n'
        return way

    elif way == 'w':
        i=i-1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 's'
        return way

    elif way == 'n':
        j=j+1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'w'
        return way

    elif way == 's':
        j=j-1
        if boundary(i, j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            way = 'e'
        return way


def go(i, j, way):

    if way == 'e':
        board[i][j]=0
        j=j+1
        print('i값',i)
        print('j값', j)
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
            print('리턴 전 i값', i)
        return i,j,way

    elif way == 'w':
        board[i][j] = 0
        j=j-1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
        return i,j,way

    elif way == 'n':
        board[i][j] = 0
        i=i+1
        if boundary(i,j) == True:
            way = 'f'
        else:
            board[i][j] = 2
        return i,j,way

    elif way == 's':
        board[i][j] = 0
        i=i-1
        if boundary(i, j) == True:
            way = 'f'
        else:
            board[i][j] = 2
        return i,j,way



board = [[0]*n for _ in range(n)]

#사과 세팅
for _ in range(k):
    a, b = map(int, input().split(' '))
    board[b-1][a-1] = 1

#방향전환 횟수
d_info = []

l = int(input())
#이동 방향 정보
for _ in range(l):
    x, c = input().split()
    d_info.append((int(x),c))

print(d_info)

sec = 0
i=0
j=0

while way!='f':

    sec = sec+1

    info_num = 0
    if sec == d_info[info_num][0]:
        info_num+=1
        print('안나완?',d_info[info_num][0])

    i,j,way = go(i,j,way)
    print(way)

    for l in range(n):
        print(board[l])


print(sec)




