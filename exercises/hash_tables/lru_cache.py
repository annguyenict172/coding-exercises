"""
Implement a LRU cache for ISBN: EPI 12.3
"""
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, max_size):
        self._lookup = OrderedDict()
        self.max_size = max_size
    
    def insert(self, isbn, price):
        if isbn in self._lookup:
            self._lookup.move_to_end(isbn)
        self._lookup[isbn] = price
        if len(self._lookup) > self.max_size:
            self._lookup.popitem(last=False)

    def lookup(self, isbn):
        if isbn in self._lookup:
            price = self._lookup[isbn]
            self._lookup.move_to_end(isbn)
            return price
        return -1
    
    def erase(self, isbn):
        if isbn in self._lookup:
            del self._lookup[isbn]
            return True
        return False


cache = LRUCache(max_size=3)
cache.insert('a', 1)
cache.insert('b', 2)
cache.insert('c', 3)
cache.lookup('a')

print(cache._lookup)