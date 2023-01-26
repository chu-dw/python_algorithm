input_word = ''
while True:
    # 굳이 List 안쓰고 name, age, weight = input().split() 으로 가능
    list = []
    input_word = input()
    if input_word == '# 0 0':
        break
    else:
        list = input_word.split(' ')
        print(list[0], end=' ')
        if (int(list[1]) > 17) or (int(list[2]) >= 80):
            print('Senior')
        else:
            print('Junior')




