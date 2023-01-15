x = int(input('x값 입력: '))
print(x == abs(x),'\n')


def diffrent(a: int, b: int) -> bool:
    return a!=b
print(diffrent(3,2),'\n')


population = int(input('인구입력: '))
land_area = int(input('지역크기: '))
density = population/land_area
if population<10000000:
    print(population)
elif 10000000 <= population <= 35000000:
    print(population)
if density > 100:
    print('densely populated')
else:
    print('sparsely populated')


ph = float(input('ph입력:'))
if 3.0 < ph < 7.0:
    print('산성입니다.\n')
elif ph <= 3.0:
    print('강산성\n')


ph2 = float(input('ph2입력:'))
if ph2 < 7.0:
    print('산성입니다.')
if ph2 < 3.0:
    print('강산성')



bmi = float(input('bmi입력'))
age = float(input('나이 입력'))
young = age < 45
heavy = bmi > 22.0
if young and heavy:
    risk = 'medium'
elif young and not heavy:
    risk = 'low'
elif not young and heavy:
    risk = "high"
elif not young and not heavy:
    risk = 'midium'

print(risk)


