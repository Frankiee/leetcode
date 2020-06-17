# [Classic, Hash]
# https://leetcode.com/problems/design-hashmap/
# 706. Design HashMap

# History:
# 1.
# Mar 17, 2019
# 2.
# Dec 2, 2019

# Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value
# already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if
# this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains
# the mapping for the key.
#
# Example:
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)
#
# Note:
#
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.


from collections import defaultdict


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10001
        self.dp = defaultdict(list)

    def _get_slot(self, key):
        return key % self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        slot = self._get_slot(key)

        for i, (k, v) in enumerate(self.dp[slot]):
            if k == key:
                self.dp[slot][i] = (key, value)
                return

        self.dp[slot].append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no
        mapping for the key
        :type key: int
        :rtype: int
        """
        slot = self._get_slot(key)

        if self.dp[slot]:
            for k, v in self.dp[slot]:
                if k == key:
                    return v

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        slot = self._get_slot(key)

        if self.dp[slot]:
            for i, (k, v) in enumerate(self.dp[slot]):
                if k == key:
                    self.dp[slot].pop(i)
                    return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
