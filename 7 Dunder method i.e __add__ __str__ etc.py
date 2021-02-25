class Employee:
    increment = 1.5  # class variable

    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal

    def __add__(self, other):
        group1 = []
        group2 = []
        group3 = []
        group = input('Enter name of group in which you want to  add those two member: ')
        if group == 'group1':
            group1.append(self)
            group1.append(other)
            print(group1)

        return f'member added and salary of group is {self.salary + other.salary}'

    def __str__(self):
        return self.fname


ganesh = Employee('Ganesh', 'Bhaip', 50000)
aniket = Employee('aniket', 'sawant', 50000)

print(aniket, ganesh)  # __str__
print(ganesh + aniket)  # __add__
