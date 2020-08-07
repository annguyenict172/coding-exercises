"""
Convert between intergers and strings: EPI 6.1
"""


def string_to_int(string):
    is_negative = string[0] == '-'
    number = 0
    for i, digit_char in enumerate(reversed(string)):
        if digit_char != '-':
            digit_value = ord(digit_char) - 48
            number += digit_value * (10 ** i)
    if is_negative:
        number = -number

    return number


def int_to_string(integer):
    if integer == 0:
        return '0'

    is_negative = integer < 0
    if is_negative:
        integer = -integer
    string = []

    while integer > 0:
        last_digit = integer % 10
        string.append(chr(last_digit+48))
        integer = int((integer - last_digit) / 10)

    if is_negative:
        string.append('-')

    return ''.join(reversed(string))
