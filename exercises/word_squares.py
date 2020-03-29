"""
Leet Code #425
"""

import unittest
import collections


class Solver:
    def word_squares(self, words):
        self.words = words
        self.length = len(words[0])
        self.prefixes = self.build_prefix_hash_table()
        results = []

        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)

        return results

    def backtracking(self, step, word_squares, results):
        if step == self.length:
            results.append(word_squares[:])
            return

        prefix = ''.join([w[step] for w in word_squares])
        for candidate in self.get_words_with_prefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step + 1, word_squares, results)
            word_squares.pop()

    def build_prefix_hash_table(self):
        prefixes = collections.defaultdict(list)
        for word in self.words:
            for i in range(1, self.length):
                prefixes[word[0:i]].append(word)
        return prefixes

    def get_words_with_prefix(self, prefix):
        return self.prefixes[prefix]


class TestResult(unittest.TestCase):

    def test_two_word_squares_list(self):
        words = ["area", "lead", "wall", "lady", "ball"]
        expected = [
            ["wall", "area", "lead", "lady"],
            ["ball", "area", "lead", "lady"]
        ]
        self.assertEqual(Solver().word_squares(words), expected)
