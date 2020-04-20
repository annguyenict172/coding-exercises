"""
The parity of a word is 1 if there is an even number of 1s, else 0
Ex:
- 11001100 -> 0
- 11100000 -> 1
"""
import unittest


# Go through one bit at a time
def parity_brute_force(x):
    result = 0
    while x != 0:
        result = result ^ (x & 1)
        x >>= 1
    return result


# Use bit manipulation trick: x & (x-1) to remove the lowest set bit
# Ex: 11001100 & 11001011 = 11001000
def parity_with_trick(x):
    result = 0
    while x != 0:
        result = result ^ 1
        x = x & (x-1)
    return result


# Break a large word into chunks, compute the parity for each chunks
# Ex: Parity 11001100 = parity(11) ^ parity(00) ^ parity(11) ^ parity(00)
CACHE = [0] * (2**16)
for i in range(0, 2**16):
    CACHE[i] = parity_with_trick(i)


def parity_with_cache(x):
    mask_size = 16
    # We need the mask to get the least 16 significant bits
    mask = 2 ** 16 - 1
    return CACHE[x >> (mask_size * 3)] ^ CACHE[x >> (mask_size * 2) & mask] \
        ^ CACHE[x >> mask_size & mask] ^ CACHE[x & mask]


# Optimal solution: use XOR to halve the input size in each step
# Ex: Parity 11001100 = Parity (1100 ^ 1100 = 0000)
# Parity 0000 = Parity (00 ^ 00 = 00)
# Parity 00 = Parity (0 ^ 0 = 0)
# Parity 0 = 0 & 1

def parity_xor(x):
    x = x ^ x >> 32
    x = x ^ x >> 16
    x = x ^ x >> 8
    x = x ^ x >> 4
    x = x ^ x >> 2
    x = x ^ x >> 1
    return x & 1


class TestResult(unittest.TestCase):

    def test_one_parity_brute_force(self):
        self.assertEqual(parity_brute_force(1), 1)

    def test_zero_parity_brute_force(self):
        self.assertEqual(parity_brute_force(3), 0)

    def test_one_parity_with_trick(self):
        self.assertEqual(parity_with_trick(1), 1)

    def test_zero_parity_with_trick(self):
        self.assertEqual(parity_with_trick(3), 0)

    def test_one_parity_with_cache(self):
        self.assertEqual(parity_with_cache(1), 1)

    def test_zero_parity_with_cache(self):
        self.assertEqual(parity_with_cache(3), 0)

    def test_one_parity_xor(self):
        self.assertEqual(parity_xor(1), 1)

    def test_zero_parity_xor(self):
        self.assertEqual(parity_xor(3), 0)
