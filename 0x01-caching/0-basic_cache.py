#!/usr/bin/python3
""" caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ defines basic caching """


    def put(self, key, item):
        """assign item value for key to dict"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ get key value from dict """
        if key is None or self.cache_data.get(key) is None:
            return None

        else:
            return self.cache_data[key]

