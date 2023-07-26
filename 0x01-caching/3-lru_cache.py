#!/usr/bin/env python3
""" caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class imprints from BaseCaching """

    def __init__(self):
        """calling the parent init"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """LRU algorithm """
        if key is None or item is None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
