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
    def change_increment(cls, inc):
        cls.increment = inc

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


class programmer(Employee):
    def __init__(self, namef, namel, sal, lang, exp):
        super().__init__(namef, namel, sal)
        self.language = lang
        self.exp = exp


sujit = programmer('sujit', 'gosavi', 500000, 'python', '9 months')
print(sujit.salary, sujit.exp)
