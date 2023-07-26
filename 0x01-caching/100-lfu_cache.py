#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching
from collections import defaultdict
import heapq

class LFUCache(BaseCaching):
    """ LFUCache defines a caching system using LFU algorithm """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)  # Track item frequency
        self.usage_count = 0  # Track the access time (LRU)
        self.min_heap = []  # Priority queue to keep track of items by frequency and LRU

    def update_frequency(self, key):
        """ Update the frequency for a key """
        self.frequency[key] += 1
        self.usage_count += 1
        heapq.heappush(self.min_heap, (self.frequency[key], self.usage_count, key))

    def put(self, key, item):
        """ Modify cache data with LFU algorithm """
        if key is None or item is None:
            return

        # Check if cache limit is reached
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            while self.min_heap:
                _, _, discard_key = heapq.heappop(self.min_heap)
                if discard_key in self.cache_data:
                    del self.cache_data[discard_key]
                    del self.frequency[discard_key]
                    break

        # Add the new item to the cache
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            self.update_frequency(key)

    def get(self, key):
        """ Retrieve value from cache data """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)  # Successful cache hit (update frequency)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Display current cache content """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")

