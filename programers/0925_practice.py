
def solution(s):
    answer = 0
    alpha_dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    for i in alpha_dic.items():
        s = s.replace(i[1],str(i[0]))

    return s

s = str(input())
answer = solution(s)
print(answer)





