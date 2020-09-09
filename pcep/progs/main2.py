# main.py

from sys import path

path.append('../modules')
#path.insert('..\\modules')

import module2

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module2.suml(zeroes))
print(module2.prodl(ones))