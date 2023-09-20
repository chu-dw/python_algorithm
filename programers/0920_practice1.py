import operator


def solution(N, stages):
    answer = []
    nonPass = len(stages)
    dic = {}

    for i in range(N + 1, 0, -1):
        # print('---stage :',i,'----')

        count_s = stages.count(i)
        # print('도착한사람',count_s)

        nonPass -= count_s
        # print('아직 아래있는 사람',nonPass)

        clear = len(stages) - nonPass
        # print('클리어 한사람', clear)

        if clear == 0:
            fail_rate = 0
        else:
            fail_rate = count_s / clear

        # print('실패율',fail_rate)
        if i != N + 1:
            dic[i] = fail_rate

    dic = dict(sorted(dic.items(), key=lambda item: (-item[1], item[0])))
    answer = list(dic.keys())

    return answer

print('n값을 입력 해주세요')
n = int(input())
print('스테이지에 도전하고 있는 사용자 수를 입력해 주세요')
stage = list(map(int,input().split()) )
print(stage)

answer = solution(n,stage)
print(answer)