def triple(num1: int) -> int:
    """num1 3배 하여 리턴"""
    return num1*3

def abs_subVal(num1: int, num2: int)->int:
    """num1 - num2 결과 절대값 리턴"""
    return abs(num1 - num2)

def change_mile(km: float)->float:
    return km/1.6

def avg(num1:int, num2:int, num3:int) -> int:
    return (num1+num2+num3) /3

def four_avg(num1: int, num2: int, num3: int, num4: int) -> int:
    first = max(num1,num2,num3,num4)
    second = min(max(num1, num2), max(num3,num4))
    third = max(min(num1, num2),min(num3,num4))
    return avg(first,second,third)

def weeks_elapsed(day1: int, day2: int) -> int:
    dif = day2 - day1
    return int(dif/7)

def square(num: int) -> int:
    return num**2

test1 = triple(2)
print(test1)

test2 = abs_subVal(2,5)
print(test2)

test3 = change_mile(160)
print(test3)

test4 = avg(3,3,3)
print(test4)

test5 = four_avg(1,10,3,5)
print(test5)

test6 = weeks_elapsed(3,20)
print(test6)

test7 = square(3)
print(test7)