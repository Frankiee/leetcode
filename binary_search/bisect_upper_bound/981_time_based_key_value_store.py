# [Bisect-Upper-Bound]
# https://leetcode.com/problems/time-based-key-value-store/
# 981. Time Based Key-Value Store

# History:
# Facebook, Netflix
# 1.
# Mar 19, 2020
# 2.
# May 5, 2020

# Create a timebased key-value store class TimeMap, that supports two operations.
#
# 1. set(string key, string value, int timestamp)
#
# Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)
#
# Returns a value such that set(key, value, timestamp_prev) was called previously,
# with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").
#
#
# Example 1:
#
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],
# ["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:
# TimeMap kv;
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
# kv.get("foo", 1);  // output "bar"
# kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3
# and timestamp 2, then the only value is at timestamp 1 ie "bar"
# kv.set("foo", "bar2", 4);
# kv.get("foo", 4); // output "bar2"
# kv.get("foo", 5); //output "bar2"
#
# Example 2:
#
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love",
# "high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]
#
#
# Note:
#
# All key/value strings are lowercase.
# All key/value strings have length in the range [1, 100]
# The timestamps for all TimeMap.set operations are strictly increasing.
# 1 <= timestamp <= 10^7
# TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per
# test case.


from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not self.store[key]:
            return ""

        l, r = 0, len(self.store[key])

        while l < r:
            m = (r - l) / 2 + l

            if self.store[key][m][0] > timestamp:
                r = m
            else:
                l = m + 1

        return self.store[key][l - 1][1] if l >= 1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


from collections import defaultdict


class TimeMap2(object):
    def _bisect(self, lst, timestamp):
        l, r = 0, len(lst)

        while l < r:
            m = (r - l) / 2 + l

            if lst[m][1] > timestamp:
                r = m
            else:
                l = m + 1

        return l

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        pos = self._bisect(self.store[key], timestamp)
        pos -= 1
        if pos < 0:
            return ""
        return self.store[key][pos][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
