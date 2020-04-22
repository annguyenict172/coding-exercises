"""
Recursive Multiply: write a recursive function to multiply two integers, without
using the * operator. You can use +, - and bit shifting.

Example:
Input:
12
5
Output:
60

"""

from io import StringIO
import unittest


def multiply(stdin):
    x = y = 0
    for line_no, line in enumerate(stdin):
        if line_no == 0:
            x = int(line)
        if line_no == 1:
            y = int(line)

    if x >= y:
        return multiply_recursive(x, y)
    else:
        return multiply_recursive(y, x)


def multiply_recursive(x, y):
    if x == 0 or y == 0:
        return 0
    if y == 1:
        return x
    if y & 1 == 1:
        return x + multiply_recursive(x << 1, (y-1) >> 1)
    else:
        return multiply_recursive(x << 1, y >> 1)


class TestResult(unittest.TestCase):

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(StringIO('0\n1000\n')), 0)
        self.assertEqual(multiply(StringIO('1000\n0\n')), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(StringIO('1000\n1\n')), 1000)
        self.assertEqual(multiply(StringIO('1\n1000\n')), 1000)

    def test_multiply_small_numbers(self):
        self.assertEqual(multiply(StringIO('3\n5\n')), 15)

    def test_multiply_big_numbers(self):
        self.assertEqual(multiply(StringIO('29192\n29391\n')), 857982072)
