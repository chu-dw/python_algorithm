from typing import List

velocities = [0.0, 9.81, 19.62, 29.43]
for val in velocities:
    print(val)

country = 'Unites States of America'
for ch in country:
    if ch.isupper():
        print(ch)

for num in range(10):
    print(num)

print(list(range(2000, 2050, 4)))

total = 0
total2 = 0
for i in range(1,101):
    total = total + i
print(total)

values = [4, 5 ,3, 1, 8]
for i in range(len(values)):
    print(i, values[i])

metals = ['Li','Na','N']
weight = [6.941, 22.986, 39.0983]
for i in range(len(metals)):
    print(metals[i],weight[i])

for i in range(10):
    for j in range(10):
        print(i,'*',j,'=',i*j)

elements = [['Li','Na', 'K'],['F','Cl','Br']]
for inner_list in elements:
    for item in inner_list:
        print(item)
    print('분류')

num = 3
while num > 0:
    print(num)
    num = num-1

text = ""
while text != 'quit':
    text = input('입력: ').lower()
    if text == 'H2O':
        print('물\n')

calegans = ['Emb', 'Him', 'Unc', 'Lon']
for i in calegans:
    print(i)

alkaline_earth_metals = [[4,9.012],[88,226],[12,24.305],[20,40.078]]
for i in alkaline_earth_metals:
    print(i)

pop = 0
country = [1295, 23, 7, 3, 47, 21]
for i in range(len(calegans)):
    pop = pop +country[i]

print(pop)

rat1 = [10, 11, 9, 10, 12]
rat2 = [12, 9, 11, 13, 13]
if rat1[0] > rat2[0]:
    print("첫 날 생쥐1 이 더 무겁")
else:
    print('첫 날 생쥐2 더 무겁')
if rat1[0] > rat2[0] and rat1[-1] > rat2[-1]:
    print('여전히 생쥐1 무겁')
else:
    print('생쥐2 더 무거워 짐')

for i in range(33,50):
    print(i)

for i in range(10):
    print(10-i,'' ,end='')

sum=0
for i in range(2,23):
    sum = sum + i
average = sum/len(range(2,23))
print(average)


def remove_neg(num_list : List[float]) -> None:
    i = 0
    while i<len(num_list):
        if num_list[i] < 0:
            del num_list[i]
        else:
            i = i+1


ex = [1,2,3,-3,-1,5]
remove_neg(ex)
print(ex)

for i in range(7):
    for j in range(0,i+1):
        print('T',end='')
    print()

for width in range(1,8):
    print('O'*width)

for i in range(1,8):
    print(' '*(8-i),'T'*i)



