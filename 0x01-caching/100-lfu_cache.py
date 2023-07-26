#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """ LFUCache defines a caching system using LFU algorithm """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)  # Track item frequency
        self.usage_count = 0  # Track the access time (LRU)

    def update_frequency(self, key):
        """ Update the frequency of a key """
        self.frequency[key] += 1
        self.usage_count += 1

    def put(self, key, item):
        """ Modify cache data with LFU algorithm """
        if key is None or item is None:
            return

        # Check if cache limit is reached
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequency used item(s)
            min_frequency = min(self.frequency.values())
            least_frequency_items = [k for k, v in self.frequency.items() if v == min_frequency]

            # If there is more than one item with the least frequency,
            # use LRU to break the tie
            if len(least_frequency_items) > 1:
                least_recently_used_item = min(least_frequency_items, key=lambda k: self.usage_count - self.frequency[k])
            else:
                least_recently_used_item = least_frequency_items[0]

            # Discard the least frequency used item
            print(f"DISCARD: {least_recently_used_item}")
            del self.cache_data[least_recently_used_item]
            del self.frequency[least_recently_used_item]

        # Add the new item to the cache
        self.cache_data[key] = item
        self.update_frequency(key)

    def get(self, key):
        """ Retrieve value from cache data """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Display current cache content """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")

