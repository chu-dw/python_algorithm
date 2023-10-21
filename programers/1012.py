import collections
def solution(k, tangerline):
    answer = 0
    cnt = collections.Counter(tangerline)

    for t in sorted(cnt.values(), reverse=True):
        k -= t
        answer += 1
        if k <= 0:
            break
    return answer

k = int(input())
tan = list(input().split())
result = solution(k,tan)
print(result)

