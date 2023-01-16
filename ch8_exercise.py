kingdoms = ['bacteria', 'protozoa', 'chromista', 'plantae', 'fungi', 'animlia']
print(kingdoms[0])
print(kingdoms[-1])
print(kingdoms[0:3])
print(kingdoms[2:4])
print(kingdoms[-1:-2])
print(kingdoms[-5])

appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
plus = appointments + ['16:30']
print(plus)
print(appointments)
appointments.append('16:30')
print(appointments)

ids = ['4353', '2314', '2956', '3382', '9362', '3900']
del ids[3]
print(ids.index('9362'))
ids.insert(ids.index('9362')+1,'4499')
print(ids)
ids.reverse()
print(ids)
ids.sort()
print(ids)

alkaline_earth_metals = [4,12,20,38,56,88]
print(alkaline_earth_metals[5])
print(alkaline_earth_metals[-1])
print('개수:',len(alkaline_earth_metals))
print('최대', max(alkaline_earth_metals))

temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
temps.sort()
print(temps)
cool_temps = temps[:2]
warm_temps = temps[2:]
print(cool_temps)
print(warm_temps)
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

def same_first_last(L: list) -> bool:
    if L[0] == L[-1]:
        return True
    else:
        return False

print(same_first_last([3,4,2,8,3]))

units = [['km','miles','league'], ['kg','pound','stone']]
print(units[0])
print(units[-1])
print(units[0][0])
print(units[1][0])
print(units[0][1:])
print(units[1][:2])