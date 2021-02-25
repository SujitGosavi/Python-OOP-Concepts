class Employee:
    increment = 1.5  # class variable

    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal
        self.day = 'monday'

    def increase_sal(self):
        self.salary = self.salary * Employee.increment

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def is_open(day):
        if day == 'sunday':
            return False
        else:
            return True


ganesh = Employee('Ganesh', 'Bhaip', 50000)
aniket = Employee.from_str("aniket-sawant-200000000")

print(ganesh.is_open(ganesh.day))  # we can use this staticmethod with object
print(ganesh.is_open('monday'))  # we can use this staticmethod with object

print(Employee.is_open('sunday'))  # we can also use this staticmethod separately with class
