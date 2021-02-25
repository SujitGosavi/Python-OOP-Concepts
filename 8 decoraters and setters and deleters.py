class Employee:

    def __init__(self, namef, namel, sal):
        self.fname = namef  # instance variable
        self.lname = namel
        self.salary = sal
        self.day = 'monday'

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Please set your first and last name"
        else:
            return self.fname + '.' + self.lname + '@gmail.com'

    @email.setter
    def email(self, given_email):
        email = given_email.split('@')[0].split('.')
        self.fname = email[0]
        self.lname = email[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


ganesh = Employee('Ganesh', 'Bhaip', 50000)
aniket = Employee('aniket', 'sawant', 50000)

print(ganesh.email)
ganesh.fname = 'chutiyaa'
print(ganesh.email)
del ganesh.email
# ganesh.fname = 'chuutiya'
# ganesh.lname = 'giri'
print(ganesh.email)
