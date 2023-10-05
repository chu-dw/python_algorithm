def solution(array, commands):
    answer = []

    loop = len(commands)
    for l in range(loop):
        i = commands[l][0]
        j = commands[l][1]
        k = commands[l][2]
        # print(i,j,k)
        ary = array[i - 1:j]
        ary.sort()
        # print('ary',ary)
        answer.append(ary[k - 1])


    return answer


i=0

array = list(map(int,input().split()))
print(array)

n = int(input('command 개수를 입력 해주세요'))
commands = [ [0 for j in range(3)] for i in range(n) ]

for i in range(n):
    commands[i].append( list(map(int, input().split())) )
    i += 1

    print(commands[i])

print(commands)
