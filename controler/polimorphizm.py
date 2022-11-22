# множественное наследование

class A:
    def hello(self):
        print("A")

class B(A):

    def __len__(self):
        return 100

    def hello(self):
        print("B")

class C(B):
    def hello(self):
        print("C")

o = A()
o.hello()