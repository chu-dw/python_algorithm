n, m = map(int,input().split())

board = [[0 for col in range(50)] for row in range(50)]


for i in range(n):
    board[i] = list(map(int, str(input())))

count = 0
index = 0
for i in range(n):
    for j in range(m):
        for l in range(m):
            if board[i][j] == board[i][l] and j!=l:
                count = l-j + 1
                # print("test")
                # print("i j",i,j)
                # print("i l",i,l)
                print(count)
                if board[i+(count-1)][l] == board[i][l] and board[i+(count-1)][j] == board[i][l]:
                    print(count*count)
                    index = 1
                    exit()

# for i in range(n):
#     print(board[i])

if index == 0:
    print(1)
