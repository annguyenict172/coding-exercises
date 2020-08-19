"""
Swap Bits: EPI 4.2
"""


def swap_bits(x, i, j):
    bit_at_i = (x >> i) & 1
    bit_at_j = (x >> j) & 1
    if bit_at_i != bit_at_j:
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x


assert swap_bits(13, 1, 0) == 14
