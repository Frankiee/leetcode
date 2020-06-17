# [Last-Element-Replace, Classic]
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# 381. Insert Delete GetRandom O(1) - Duplicates allowed

# History:
# Apple
# 1.
# Mar 21, 2020
# 2.
# May 8, 2020

# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of
# each element being returned is linearly related to the number of same value the collection
# contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection
# now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();


from collections import defaultdict


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = defaultdict(set)
        self.lst = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain
        the specified element.
        :type val: int
        :rtype: bool
        """
        self.lst.append(val)
        self.mp[val].add(len(self.lst) - 1)

        return len(self.mp[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the
        specified element.
        :type val: int
        :rtype: bool
        """
        if len(self.mp[val]) == 0:
            return False

        idx = self.mp[val].pop()
        if not self.mp[val]:
            del self.mp[val]

        if idx == len(self.lst) - 1:
            self.lst.pop(-1)
        else:
            val = self.lst.pop(-1)
            self.mp[val].remove(len(self.lst))
            self.lst[idx] = val
            self.mp[val].add(idx)

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
