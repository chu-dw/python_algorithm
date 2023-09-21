def solution(s, skip, index):
    answer = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"

    for sk in skip:
        if sk in alpha:
            alpha = alpha.replace(sk, "")



    a_len = len(alpha)

    # print('a',alpha)
    # print("a_len", a_len)

    for i in s:
        if i in alpha:
            change = alpha[(alpha.index(i) + index) % a_len]
            answer += change
        else:
            answer = "오류입니다"
            break

    print(answer)

    return answer


print('조건 3개를 입력 해주세요')
s, skip, index = input().split()
index = int(index)

#aukks wbqd  5
output = solution(s, skip, index)
print(output)