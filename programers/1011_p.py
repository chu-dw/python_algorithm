import collections
def solution(k, tangerline):
    answer = 0
    cnt = collections.Counter(tangerline)
    print(cnt)

    for i in sorted(cnt.values(), reverse=True):
        print(i)
        k -= i
        answer += 1
        if k <= 0:
            break
    print(answer)
    return answer


k = int(input())
tan = list(input().split())

answer = solution(k,tan)
print('답 : ', answer)