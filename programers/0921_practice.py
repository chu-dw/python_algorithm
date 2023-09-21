def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        # print(survey[i], choices[i])
        q_list = list(survey[i])
        # print(q_list)

        if choices[i] > 4:
            score[q_list[1]] += choices[i] - 4
        elif choices[i] < 4:
            score[q_list[0]] += 4 - choices[i]
    # print(score)

    score_li = list(score.items())
    # print('list test', score_li)

    for i in range(0, 8, 2):

        # print(score_li[i][1], score_li[i+1][1])
        if score_li[i][1] > score_li[i + 1][1]:
            answer += score_li[i][0]

        elif score_li[i][1] < score_li[i + 1][1]:
            answer += score_li[i + 1][0]

        else:
            answer += score_li[i][0]

    return answer

print("survey입력")
survey = list(input().split())
print("choice입력")
choice = list(map(int,input().split()))

#print(survey, choice)

answer = solution(survey,choice)
print(answer)