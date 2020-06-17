# [Classic, Hash]
# https://leetcode.com/problems/design-hashset/
# 705. Design HashSet

# History:
# 1.
# Aug 12, 2019
# 2.
# Dec 2, 2019

# Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist
# in the HashSet, do nothing.
#
# Example:
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)
#
# Note:
#
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.


from collections import defaultdict


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10001
        self.dp = defaultdict(list)

    def _get_slot(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        slot = self._get_slot(key)

        for i in self.dp[slot]:
            if i == key:
                return

        self.dp[slot].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        slot = self._get_slot(key)

        if self.dp[slot]:
            for i, val in enumerate(self.dp[slot]):
                if val == key:
                    self.dp[slot].pop(i)
                    return

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        slot = self._get_slot(key)

        if self.dp[slot]:
            for i in self.dp[slot]:
                if i == key:
                    return True

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
