#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines an intro to use cache """
    def put(self, key, item):
        """ Modify cache data """
        if key is not None and item is not None:
            self.cache_data[key] = item
        elif key in self.cache_data and item is None:
            del self.cache_data[key]

    def get(self, key):
        """ Retrieve value from cache data """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Display current cache content """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")

