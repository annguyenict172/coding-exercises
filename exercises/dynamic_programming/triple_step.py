"""
Triple Steps: a child can hop 1, 2 or 3 steps at a time
How many ways can he/she jump to n steps?

Sample Input:
3

Sample Output:
10
"""

from io import StringIO
import unittest


def triple_step(stdin):
    num_of_steps = 0

    for line in stdin:
        num_of_steps = int(line)

    if num_of_steps <= 0:
        return 0
    elif num_of_steps <= 2:
        return num_of_steps
    elif num_of_steps == 3:
        return 4
    else:
        ways = [0] * (num_of_steps + 1)
        ways[1] = 1
        ways[2] = 2
        ways[3] = 4

        for i in range(4, num_of_steps+1):
            ways[i] = ways[i-3] + ways[i-2] + ways[i-1]

        return ways[num_of_steps]


class TestResult(unittest.TestCase):

    def test_zero_step(self):
        self.assertEqual(triple_step(StringIO('0\n')), 0)

    def test_four_steps(self):
        self.assertEqual(triple_step(StringIO('4\n')), 7)

    def test_five_steps(self):
        self.assertEqual(triple_step(StringIO('5\n')), 13)

    def test_six_steps(self):
        self.assertEqual(triple_step(StringIO('6\n')), 24)
