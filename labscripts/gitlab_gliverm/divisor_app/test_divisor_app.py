#!/usr/bin/env python

# Run this by cd'ing into the directory
#   python3 -m unittest -v test_divisor_app.py

from divisors_app import *
import unittest
from unittest.mock import MagicMock, patch

#Initial Test Class
class TestDivisorApp(unittest.TestCase):
    
    def setUp(self):
        #self.divisors = divisors_app.Divisors()
        self.divisors = Divisors()

    # Take input from user - set_user_num
    def test_set_user_num(self):
        expected_num = 10
        # The unittest.mock.patch method will replace standard input method
        #   with the values of side_affect.  When app prompts the user for
        #   a value our test will automatically provide this value.
        with patch('builtins.input', side_effect=['10']):
            self.divisors.set_user_num()

        self.assertEqual(self.divisors.user_num, expected_num)

    # Generate divisors and store in object
    def test_generate_divisors(self):
        control_number = 10
        expected_divisors = [1,2,5,10]
        with patch('builtins.input', side_effect=[control_number]):
            self.divisors.set_user_num()
            self.divisors.generate_divisors()
        self.assertEqual(self.divisors.divisors, expected_divisors)


