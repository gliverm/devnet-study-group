print(1/1)
print(1//2*3)
print(1/2+3//3+4**2)
print(2+3*5.)
print(20.12E8)
print("3"*6)

x=11
y=4
x = x%y
x = x%y
y = y%x
print(y)

x = 2/4
print(4/x)

# x = 2 // 4
# print(4//x)

nums= [1,2,3]
vals = nums
del vals[1:2]
print(vals)

def any():
    print(var + 1, end='')
var = 1
any()
print(var)

dct = {}
lst = ['a', 'b', 'c', 'd']
for i in range(len(lst) -1):
    dct[lst[i]] = ( lst[i], )
for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])

def fun(x,y,z):
    return x+2*y+3*z
print(fun(0, z=1, y=3))

def f(x):
    if x == 0:
        return 0
    return x +f(x-1)
print(f(3))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
# print(fun(fun(2))+1)

def fun(x):
    x += 1
    return x

x = 2
x = fun(x+1)
print(x)

def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)

def func1(a):
    return a ** a
def func2(a):
    return func1(a) * func1(a)
print(func2(2))

tup = 1,2,4,8
tup = tup[1:-1]
tup = tup[0]
print(tup)

print("Mike" > "Mikey")