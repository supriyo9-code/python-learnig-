class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am a class variable in class B"
    def __init__(self):
        #super().__init__()
        self.var1 = "I am inside B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()


a = A()
b = B()

print(b.special, b.var1, b.classvar1)