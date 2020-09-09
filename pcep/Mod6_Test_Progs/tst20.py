class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a, 'A'))

# raises exception becaues no parameter in initialization of A