"""
Base Conversion: EPI 6.2
"""


def is_big_letter(char):
    if 55 <= ord(char) <= 70:
        return True
    return False


def convert_base(num, b1, b2):
    value = 0

    for i, char in enumerate(num):
        if is_big_letter(char):
            digit_value = ord(char) - 55
        else:
            digit_value = ord(char) - 48

        value += digit_value * b1**(len(num)-1-i)

    num_in_b2 = []
    while value > 0:
        last_digit = value % b2
        if last_digit > 9:
            num_in_b2.append(chr(last_digit + 55))
        else:
            num_in_b2.append(chr(last_digit + 48))

        value = value // b2

    return "".join(reversed(num_in_b2))


print(convert_base('1AF', 16, 2))
