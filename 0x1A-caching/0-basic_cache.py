#!/usr/bin/python3
"""
module 0
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class basiccache
    """
    def put(self, key, item):
        """
        put function
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        get
        """
        if key and self.cache_data.get(key):
            return self.cache_data[key]
        return None
