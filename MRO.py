class A:
    def some_method(self):
        print('Mechod of class A')

class B(A):
    def some_method(self):
        print('Mechod of class B')

class C(A):
    def some_method(self):
        print('Mechod of class C')

class D(B, C):
    pass
    #def some_method(self):
        #print('Mechod of class D')

print(D.__mro__)

obj = D()
obj.some_method()