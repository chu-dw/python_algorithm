input_str = input()
print(input_str)
print(input_str[2])
print(input_str[2].isdigit())
num = []
str = []

for i in range(len(input_str)):
    if input_str[i].isdigit() == True:
        num.append(input_str[i])

    elif input_str[i].isdigit() == False:
        str.append(input_str[i])

print(*(str + num),sep='')