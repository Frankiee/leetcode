# [OrderedDict, Classic]
# https://leetcode.com/problems/lru-cache/
# 146. LRU Cache

# History:
# Facebook, Dropbox
# 1.
# Feb 6, 2020

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support
# the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
# otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache
# reached its capacity, it should invalidate the least recently used item before inserting a new
# item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3347, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


from collections import OrderedDict


# Python 3 Required
class LRUCacheOrderedDict:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mem = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        item = self.mem.get(key)

        if item:
            self.mem.move_to_end(key, last=False)

        return item or -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.mem[key] = value
        self.mem.move_to_end(key, last=False)

        if len(self.mem) > self.capacity:
            self.mem.popitem()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node(object):
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCacheDoubleLinkedList(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0

        self.lst = Node(None, None)
        second = Node(None, None)
        self.lst.nxt = second
        second.prev = self.lst
        self.end = second

        self.mp = {}

    def _push_to_front(self, node):
        first = self.lst.nxt
        self.lst.nxt = node
        node.prev = self.lst

        node.nxt = first
        first.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mp:
            return -1

        node = self.mp[key]

        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        self._push_to_front(node)

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.mp:
            self.mp[key].val = value
            node = self.mp[key]

            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

            self._push_to_front(node)
        else:
            self.mp[key] = Node(key, value)
            self._push_to_front(self.mp[key])
            self.size += 1

        if self.size > self.capacity:
            to_remove = self.end.prev

            prev = to_remove.prev
            prev.nxt = self.end
            self.end.prev = prev

            del self.mp[to_remove.key]
            self.size -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
