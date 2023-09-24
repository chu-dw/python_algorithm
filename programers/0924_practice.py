

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {}
    for i in id_list:
        reports[id] = 0

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= 4:
            answer[id_list.index(r.split()[0])] += 1

    return answer



id_list = list(input())
report = list(input())
k = int(input())

answer = solution(id_list, report, k)
print(answer)