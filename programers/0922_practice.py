# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]

def solution(lottos, win_nums):
    answer = []
    cnt_o = lottos.count(0)
    count = 0

    rank = [6,6,5,4,3,2,1]
    for lo in lottos:
        if lo in win_nums:
            count += 1

    answer = [rank[count+cnt_o],rank[count]]
    return answer

lottos = list(map(int,input().split()))
win_num = list(map(int,input().split()))

answer = solution(lottos,win_num)
print(answer)