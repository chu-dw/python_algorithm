import math
import calendar

no1 = math.floor(-2.8)
print(no1)
no2 = math.fabs(round(-4.3))
print(no2)
no3 = math.ceil(math.sin(34.5))
print(no3,'\n')

#help(calendar.isleap)
val = calendar.isleap(2024)
print(val)
print(dir(calendar))
leapNum = calendar.leapdays(2000,2050)
print(leapNum)
week = calendar.weekday(2016,7,29)
print((week))
