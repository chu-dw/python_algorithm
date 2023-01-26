class Member:

    def __init__(self, name: str, address:str, email:str) -> None:
        self.name = name
        self.address = address
        self.email = email

    def __str__(self) -> str:
        write = '{} {} {}'.format(self.name, self.address, self.email)
        return write


class Student(Member):

    def __init__(self, name: str, address:str, email:str, student_num: str) -> None:

        super().__init__(name, address, email)
        self.student_num = student_num

chu = Student('chu','shin','ehddnjs@daum.net','2020158047')
print(chu)



class Atom:
    def __init__(self, num: int, sym: str, x: float, y: float, z: float) -> None:
        self.number = num
        self.center = (x, y, z)
        self.symbol = sym

    def __str__(self) -> str:
        check = '({0}, {1}, {2}, {3})'.format(self.symbol, self.center[0], self.center[1], self.center[2])
        return check

    def translate(self, x:float, y:float, z:float):
        self.center = (self.center[0]+x, self.center[1]+y, self.center[2]+z)



class Molecule:
    def __int__(self, name: str) -> None:
        self.name = name
        self.automs = []

    def add(self, a: Atom) -> None:
        self.automs.append(a)


class Country:
    def __init__(self, name: str, pop: int, area: int):
        self.coutry_name = name
        self.population = pop
        self.area = area

    def is_larger(self, diff) -> bool:
        if self.area > diff.area:
            return_val = True
        else:
            return_val = False
        return return_val

canada = Country('canada', 34482779, 9984670)
print(canada.coutry_name, canada.population, canada.area)
usa = Country('usa', 313914040, 9826675)
print(canada.is_larger(usa))