

class Employee:
    increment = 1.5  # class variable
    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal

    def increase_sal(self):
        self.salary = self.salary * Employee.increment


    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)



suju = Employee.from_str("suju-gosavi-200000000")

print(suju.fname)