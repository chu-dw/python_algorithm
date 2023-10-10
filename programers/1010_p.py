numbers = list(input().split())
#어렵다 레벨 2는 아직 무린가
def solution(numbers):

    answer = [-1]*len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and stack[-1] < numbers[i]:
            big_num = stack.pop()
            answer[big_num] =numbers[i]
        stack.append(i)
    return answer

print(solution(numbers))