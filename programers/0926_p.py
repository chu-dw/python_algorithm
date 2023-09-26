def solution(s):
    answer = []
    score = [0, 0, 0]

    i1 = [1, 2, 3, 4, 5]
    i2 = [2, 1, 2, 3, 2, 4, 2, 5]
    i3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for an in range(len(s)):

        if int(s[an]) == i1[an%5]:
            score[0] += 1

        if int(s[an]) == i2[an%8]:
            score[1] += 1

        if int(s[an]) == i3[an%10]:
            score[2] += 1

    #print(score)

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer

s = list(input().split())
answer = solution(s)
print(answer)