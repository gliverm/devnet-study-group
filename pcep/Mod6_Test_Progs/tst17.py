class A:
    def __init__(self):
        self.a = 1

class B:
    def __init__(self):
        A.__init__(self)
        self.b = 2

o = B()
print("Happy happy!")