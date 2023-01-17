file = open('test1.txt','r')
contents = file.read()
file.close()
print(contents)

with open('test1.txt','r') as file:
    contents = file.read()

with open('test1.txt','r') as line_file:
    line = line_file.readlines()
print(line)

with open('planets.txt','r') as p_file:
    planets = p_file.readlines()

print(planets)
for i in reversed(planets):
    print(i.strip())

for i in sorted(planets):
    print(i.strip())

with open('planets.txt','r') as line:
    for i in line:
        print(len(i))

with open('test2.txt','r') as test2_file:
    test2_file.readline()
    data = test2_file.readline().rstrip()
    while data.startswith('#'):
        data = test2_file.readline().rstrip()
    print('넌 뭐야',data)
    for data in test2_file:
        print(data.rstrip())


with open('test3.txt','w') as test3_file:
    test3_file.write('hello')


with open('test4(input).txt', 'r') as input:
    input_txt = input.readline()
    input_txt.split()
print(input_txt[0:3])
