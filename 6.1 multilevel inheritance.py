class a:
    def fun_a(self):
        print('fun_a is working')


class b(a):
    def fun_b(self):
        print('fun_b is working')


class c(b):
    def fun_c(self):
        print('fun_c is working')


c_object = c()

c_object.fun_a()
c_object.fun_b()
c_object.fun_c()
