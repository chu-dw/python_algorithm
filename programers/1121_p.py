

def solution(park, routes):
    answer = []

    h = len(park)
    w = len(park[0])
    x,y = 0,0
    # x, y
    nav = {'N':[-1,0], 'S':[1,0], 'W':[0,-1], 'E':[0,1]}

    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for i in routes:
        direct, distance = i.split()
        distance = int(distance)
        flag = 0
        print(direct, distance)
        x_t, y_t = x, y
        print(x_t, y_t)
        for j in range(distance):
            print('2',x_t, y_t)
            x_t += nav[direct][0]
            print(nav[direct][1])
            y_t += nav[direct][1]
            if x_t < 0 or x_t > h or y_t < 0 or y_t > w or park[x_t][y_t] == 'X':
                flag = 1
                print('너군')
                break
        if flag == 0:
            x += nav[direct][0] * distance
            y += nav[direct][1] * distance

    answer = [x,y]
    return answer


park = list(input().split())
routes = list(input().split(','))

print(park, routes)

answer = solution(park, routes)
print(answer)