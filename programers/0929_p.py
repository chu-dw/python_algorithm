def solution(numbers):
    answer = -1
    num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    sum = 0

    for i in num:
        if i not in numbers:
            sum += i

    answer = sum
    return answer

num = list(map(int,(input().split())))
answer = solution(num)
print(answer)