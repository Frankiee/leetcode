# [Important]
# https://leetcode.com/problems/lfu-cache/
# 460. LFU Cache

# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


from collections import OrderedDict


class Item(object):
    def __init__(self, freq, value):
        self.freq = freq
        self.value = value


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mp = {}
        self.capacity_bins = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        item = self.mp.get(key)
        if not item:
            return -1

        capacity_bin = self.capacity_bins.get(item.freq)
        del capacity_bin[key]
        if len(capacity_bin) == 0:
            del self.capacity_bins[item.freq]

        item.freq += 1

        new_capacity_bin = self.capacity_bins.get(item.freq)

        if not new_capacity_bin:
            new_capacity_bin = OrderedDict()
            self.capacity_bins[item.freq] = new_capacity_bin

        new_capacity_bin[key] = item
        new_capacity_bin.move_to_end(key, last=False)

        return item.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.mp:
            item = self.mp[key]
            item.value = value

            capacity_bin = self.capacity_bins.get(item.freq)
            del capacity_bin[key]
            if len(capacity_bin) == 0:
                del self.capacity_bins[item.freq]

            item.freq += 1
        else:
            if len(self.mp) >= self.capacity:
                max_capacity = max(self.capacity_bins.keys())
                old_item = self.capacity_bins[max_capacity].popitem()
                del self.mp[old_item[0]]
                if len(self.capacity_bins[max_capacity]) == 0:
                    del self.capacity_bins[max_capacity]

            item = Item(freq=1, value=value)

        new_capacity_bin = self.capacity_bins.get(item.freq)

        if not new_capacity_bin:
            new_capacity_bin = OrderedDict()
            self.capacity_bins[item.freq] = new_capacity_bin

        new_capacity_bin[key] = item
        new_capacity_bin.move_to_end(key, last=False)

        self.mp[key] = item

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
