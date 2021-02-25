"""

Why use class method?
Ans : for example we want to increase the increment variable i.e class variable in a method for that we define a simple 
method in class but it will take self as an argument and we dont even use that self in that method, to avoid 'self' and
to increase the efficiency of program we use @classmethod

"""


class Employee:
    increment = 1.5  # class variable
    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal

    def increase_sal(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def change_increment(cls, inc):
        cls.increment = inc


sujit = Employee('Sujit', 'Gosavi', 100000000)

print("Original sal")
print(sujit.salary)
print()

print("executing the increase_sal function...")
sujit.increase_sal()
print()

print("sal after running increase_sal function")
print(sujit.salary)
print()

print('executing @classsmethod i.e change_increment...')
Employee.change_increment(2)
print()

print("executing the increase_sal function Again...")
sujit.increase_sal()
print()

print("sal after running increase_sal function and @classmethod i.e change_increment")
print(sujit.salary)
print()
