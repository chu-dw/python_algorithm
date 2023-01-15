print("They'll hibernate during the winter.\n")
print('"Absolutely not," he said. ("Absolutely not." , he said)\n')
print("left/right\n")
print("'''A\nB\nC'''")

str = ''
print(len(str))
print('\n')

x = 3
y = 12.5
print('The rabbit is', x)
print('The rabbit is', x, 'years old')
print(y,'is average.')
print(y,'*',x)
print(y,'*',x, 'is', y*x,'.\n')

val = input("입력: ")
print(float(val),'\n')

def repeat(s: str, n: int) -> str:
    return(s*n)
print(repeat('yes',4),'\n')

def total_length(s1: str, s2: str) -> int:
    len1 = len(s1)
    len2 = len(s2)
    return len1+len2
print(total_length('yes','no'))
