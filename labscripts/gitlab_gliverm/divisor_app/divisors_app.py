#!/usr/bin/env python

class Divisors:

    def __init__(self):
        self.user_num = 0
        self.divisors = []

    def set_user_num(self):
        self.user_num = int(input("Enter a natural number: "))

    def generate_divisors(self):
        for num in range(1, self.user_num + 1):
            if self.user_num % num == 0:
                self.divisors.append(num)

# The following to test in a python interpreter:
# >>> from divisors_app import Divisors
# >>> div = Divisors()
# >>> div.set_user_num()
# Enter a natural number: 10
# >>> div.user_num
# 10
# >>> div.generate_divisors()
# >>> div.divisors
# [1, 2, 5, 10]
