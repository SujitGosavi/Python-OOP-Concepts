class Employee:
    increament = 1.5  # class variable
    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal

    def increase_sal(self):
        self.salary = self.salary * Employee.increament

sujit = Employee('Sujit', 'Gosavi', 100000000)
print(sujit.salary)
sujit.increase_sal()
print(sujit.salary)
