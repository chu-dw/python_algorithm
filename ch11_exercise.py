from typing import TextIO, Dict
from io import StringIO

def obser_bird(observation_file: TextIO) -> set[str]:
    birds_observed = set()
    for line in observation_file:
        bird = line.strip()
        birds_observed.add(bird)

    return birds_observed

with open('test5.txt') as ob_file:
    birds_observed = obser_bird(ob_file)
    print(birds_observed)

birds_observed.add('hello')

for spec in birds_observed:
    print(spec)

bird_to_bservations = {'canada goose':3, 'northern fulmar':1}
print(bird_to_bservations)

bird_to_bservations['snow goose'] = 33
bird_to_bservations['eagle'] = 999

print(bird_to_bservations)

for i in bird_to_bservations:
    print(bird_to_bservations[i], i)

for key, val in bird_to_bservations.items():
    print('같이',key, val)

fish_observe = {'연어':3,'참가자미': 7, '기름가자미':1, '넙치':3}

observation_to_fish = {}
for fish, key in fish_observe.items():
    if key in observation_to_fish:
        observation_to_fish[key].append(fish) #이미 해당 key에 값이 있을경우
    else:
        observation_to_fish[key] = [fish] #key에 값 없을 경우

print(observation_to_fish)

for index in observation_to_fish:
    print(index,':',end = '')
    for fish in observation_to_fish[index]:
        print(fish,end = ' ')
    print()

print('-----------------------------------------------------')

def find_dups(input_list :list) -> set:
    element = set()
    dups = set()

    for index in input_list:
        intial = len(element)
        element.add(index)
        later = len(element)  #set은 중복 안되니까 이미 있는 값 들어오면 윗줄에서 add안됨 -> intial과 later값 같다
        if intial == later:
            dups.add(index)
    return dups


num = [3,5,3,1,2,4,1,9]
output = find_dups(num)
print(output)

def find_name(input_name: list) -> set:
    element = set()
    dups = set()
    for index in input_name:
        check = len(element)
        element.add(index)
        check2 = len(element)
        if check == check2:
            dups.add(index)

    return dups

name = ['kim','chu','lee','kim','jeong']
output2 = find_name(name)
print(output2)


def pairs(set1: set, set2: set) -> (set, set):
    range_loop = len(set1)
    pair = set()
    for index in range(range_loop):
        store_male = set1.pop()
        store_female = set2.pop()
        pair.add((store_male, store_female))
    return pair


males = {'a','v','s','d'}
females = {'1','2','3','4'}

sum = pairs(males,females)
print(sum)

def find_author(filename : str) -> list:
    names = set()
    with open(filename,'r') as data:
        for line in data:
            if line.lower().startswith('author'):
                name = line[6:].strip()
                names.add(name)  #list에는 add를 못쓴다 append는 가능
    return names

name_output = find_author('pdb.txt')
print(name_output)


def count_values(input: dict) -> int:
    set_to_dic = set(input.values())    #그냥 딕셔너리를 set으로 바꿔버림
    return len(set_to_dic)

only_int = count_values({'red':1, 'green':1, 'blue':2})
print(only_int)


def return_less(input: dict) -> str:  #애는 또 c처럼 푸네  // get은 key넣으면 값 나옴 -> 반대는 안됨
    small = 1
    for index in input:
        temp = input[index]   #index가 키  //  dic[incex]가 값
        if small > temp:
            small = temp
    return small


test = {'n':0.44, 'p':0.21, 'm':0.03, 'ne':1.3}
input_min = return_less(test)
print(input_min)


def count_duplication(input: dict) -> int:  #list로 만들어서 반복문 count로 비교도 가능
    output = 0
    set_store = set()
    for index in input:
        intial = len(set_store)
        set_store.add(input[index])
        check = len(set_store)
        if intial == check:
            output=output+1

    return output

dups_output = count_duplication({'1':'hello', '2':'good', '3':'hello', '4':'soso','5':'soso'})
print(dups_output)

#-----------------연습문제 8번 할 차례---------------------





