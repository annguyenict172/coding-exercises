"""
Leet Code #482
"""
import unittest


def license_key_formatting(string, k):
    if not string:
        return ''
    string_builder = []
    chars_in_group = 0
    for i in range(len(string)-1, -1, -1):
        if string[i] != '-':
            string_builder.append(string[i].upper())
            chars_in_group += 1
            if chars_in_group == k:
                string_builder.append('-')
                chars_in_group = 0

    if len(string_builder) == 0:
        return ''

    if string_builder[-1] == '-':
        string_builder.pop()

    return ''.join(list(reversed(string_builder)))


class TestResult(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(license_key_formatting('', 5), '')

    def test_k_larger_than_string_length(self):
        self.assertEqual(license_key_formatting('abcd', 5), 'ABCD')

    def test_single_group(self):
        self.assertEqual(license_key_formatting('a-bcd-efg', 7), 'ABCDEFG')

    def test_first_group_has_less_characters(self):
        self.assertEqual(license_key_formatting('a-b-cd-ef-g-h', 3), 'AB-CDE-FGH')

    def test_all_group_equal_characters(self):
        self.assertEqual(license_key_formatting('a-b-cd-ef-g-h-i', 3), 'ABC-DEF-GHI')

    def test_dash_only_string(self):
        self.assertEqual(license_key_formatting('---', 3), '')

    def test_multiple_dashes_in_beginning(self):
        self.assertEqual(license_key_formatting('---AA-AA', 2), 'AA-AA')
