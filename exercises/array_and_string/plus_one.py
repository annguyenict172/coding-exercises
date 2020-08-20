"""
Plus One: EPI 5.2
"""

# Trivial case: last digit < 9
# Edge case: last digit == 9
# Another edge case: every digit is 9


def plus_one(digits):
    last_idx = len(digits) - 1
    while last_idx >= 0:
        if digits[last_idx] < 9:
            digits[last_idx] += 1
            break
        else:
            digits[last_idx] = 0
            last_idx -= 1

    if digits[0] == 0 and last_idx == -1:
        digits[0] = 1
        digits.append(0)


digits = [9, 9, 9]
plus_one(digits)
print(digits)
