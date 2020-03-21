"""
Implementation of hash table using array and linked list
"""

import unittest

from ds_and_algo.linked_list import LinkedList


class HashTable:
    def __init__(self):
        self.size = 30
        self.array = [LinkedList() for _ in range(self.size)]

    def _hash_key_to_index(self, key):
        if type(key) is int:
            return key % self.size
        elif type(key) is str:
            num_value = 0
            for char in key:
                num_value += ord(char)
            return num_value % self.size
        else:
            raise Exception('Only strings and integers can be used as key.')

    def set(self, key, value):
        index = self._hash_key_to_index(key)
        list_at_index = self.array[index]

        updated = list_at_index.update(key, value)
        if not updated:
            list_at_index.add(key, value)

    def get(self, key):
        index = self._hash_key_to_index(key)
        list_at_index = self.array[index]
        node = list_at_index.find(key)
        if node is not None:
            return node.value

    def delete(self, key):
        index = self._hash_key_to_index(key)
        list_at_index = self.array[index]
        list_at_index.delete(key)


class TestHashTable(unittest.TestCase):

    def test_set_and_get_value(self):
        hash_table = HashTable()
        hash_table.set('An', 1)
        hash_table.set('Kin', 2)
        self.assertEqual(hash_table.get('An'), 1)
        self.assertEqual(hash_table.get('Kin'), 2)

    def test_reset_value(self):
        hash_table = HashTable()
        hash_table.set('An', 1)
        self.assertEqual(hash_table.get('An'), 1)
        hash_table.set('An', 2)
        self.assertEqual(hash_table.get('An'), 2)

    def test_hash_collision(self):
        hash_table = HashTable()

        self.assertEqual(hash_table._hash_key_to_index('An'), 25)

        hash_table.set('An', 1)
        hash_table.set(25, 2)
        self.assertEqual(hash_table.get('An'), 1)
        self.assertEqual(hash_table.get(25), 2)

    def test_delete_key(self):
        hash_table = HashTable()
        hash_table.set('An', 1)
        self.assertEqual(hash_table.get('An'), 1)
        hash_table.delete('An')
        self.assertEqual(hash_table.get('An'), None)

    def test_delete_collision_key(self):
        hash_table = HashTable()

        self.assertEqual(hash_table._hash_key_to_index('An'), 25)

        hash_table.set('An', 1)
        hash_table.set(25, 2)

        hash_table.delete('An')

        self.assertEqual(hash_table.get('An'), None)
        self.assertEqual(hash_table.get(25), 2)
