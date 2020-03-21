"""
A slightly different implementation of linked list, where each node has an
associate key and value. This change intends to make implementing hash table easier.
"""

import unittest


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key, value):
        if self.head is None:
            self.head = Node(key, value)
            self.tail = self.head
        else:
            new_node = Node(key, value)
            self.tail.next = new_node
            self.tail = new_node

    def find(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            else:
                current = current.next

    def update(self, key, value):
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return True
            else:
                current = current.next
        return False

    def delete(self, key):
        current = self.head
        previous = self.head

        if current.key == key:
            self.head = current.next
            return True

        while current is not None:
            if current.key == key:
                previous.next = current.next
                if current == self.tail:
                    self.tail = previous
                return True
            else:
                previous = current
                current = current.next
        return False


class TestLinkedList(unittest.TestCase):

    def test_add_node(self):
        linked_list = LinkedList()
        linked_list.add('key', 'value')

        added_node = linked_list.find('key')
        self.assertEqual(added_node.value, 'value')

    def test_update_node(self):
        linked_list = LinkedList()
        linked_list.add('key', 'value')

        added_node = linked_list.find('key')
        self.assertEqual(added_node.value, 'value')

        linked_list.update('key', 'value2')
        self.assertEqual(added_node.value, 'value2')

    def test_delete_at_head(self):
        linked_list = LinkedList()

        linked_list.add('head', 1)
        linked_list.add('middle', 2)
        linked_list.add('tail', 3)

        self.assertEqual(linked_list.head.value, 1)

        linked_list.delete('head')
        self.assertEqual(linked_list.head.value, 2)

    def test_delete_at_middle(self):
        linked_list = LinkedList()

        linked_list.add('head', 1)
        linked_list.add('middle', 2)
        linked_list.add('tail', 4)

        self.assertIsNotNone(linked_list.find('middle'))
        linked_list.delete('middle')

        self.assertIsNone(linked_list.find('middle'))

    def test_delete_at_tail(self):
        linked_list = LinkedList()

        linked_list.add('head', 1)
        linked_list.add('middle', 2)
        linked_list.add('tail', 3)

        self.assertEqual(linked_list.tail.value, 3)

        linked_list.delete('tail')
        self.assertEqual(linked_list.tail.value, 2)

    def test_delete_the_only_node(self):
        linked_list = LinkedList()

        linked_list.add('head', 1)

        self.assertEqual(linked_list.head.value, 1)
        self.assertEqual(linked_list.tail.value, 1)

        linked_list.delete('head')
        self.assertIsNone(linked_list.head)
