t1 = 'hello'.upper()
print(t1)
t2 = 'hello'.endswith('o')
print(t2)
t3 = 'Hello {0}! Hello {1}'.format('python','World')
print(t3)

search = 'tomato'.count('o')
print(search)

index = 'tomato'.find('o')
print(index)

index2 = 'tomato'.find('o', 'tomato'.find('o')+1)
print(index2)

avo = 'avocado'.find('o', 'avocado'.find('o')+1)
print(avo)

change = 'runner'.replace('n','b')
print(change)

seanson = 'summer'
print('i love {0}'.format(seanson))

side1 = '3'
side2 = '4'
side3 = '5'
print('the sides have length {0}, {1} and {2}\n'.format(side1, side2, side3))

input = 'boolean'
output = input.upper()
print(output)

print('CO2 H2O'.find('2'))
blank = 'CO2 H2O'


print('CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1))

print("Boolean"[0].islower())

print('MoNDaY'.capitalize())

print(' monday'.lstrip())

def total_occurences(s1: str, s2: str, ch: str) -> int:
    val = s1 + s2
    return val.count(ch)

print(total_occurences('color','yellow','l'))