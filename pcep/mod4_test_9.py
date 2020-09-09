list = ['Mary' 'had', 'a', 'little', 'lamb']

def list(lst):
    print(list[3])
    del lst[3]
    lst[3] = 'ram'

print(list(list))

# Dude list is being redefined as a function so errors out