"""
Reverse bits: EPI 4.3
"""


def reverse_bits(num):
    reverse_num = 0

    for i in range(0, 64):
        bit_at_i = num & 2**i == 2**i
        if bit_at_i:
            reverse_num += 2**(63-i)

    return reverse_num


print(reverse_bits(16))
