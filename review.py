def three (num1 :int, num2 :int, bias :str) -> int:
    if bias == '+':
        return num1 + num2
    elif bias == '-':
        return num1 - num2

# num1 = int(input('숫자 1 입력:'))
# str = str(input('부호입력: '))
# num2 = int(input('숫자 2 입력:'))

# print('결과:',three(num1,num2,str))


index = 'tomatado'.find('o', 'tomatado'.find('o')+1)
print(index-1)

index2 = 'CO2 H2O'.find('2','CO2 H2O'.find('2')+1)
print(index2)

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
cold = []
warm = []
temps.sort()
print(temps)
for i in range(0,len(temps)):
    if int(temps[i]) <= 20:
        cold.append(temps[i])
    elif int(temps[i] > 20):
        warm.append(temps[i])

print('clod:',cold)
print('warm:', warm)
