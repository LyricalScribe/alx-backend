#!/usr/bin/python3
""" caching system """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class imprints from BaseCaching """

    def __init__(self):
        """calling the parent init"""
        super().__init__()

    def put(self, key, item):
        """FIFO algorithm """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """
        returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
