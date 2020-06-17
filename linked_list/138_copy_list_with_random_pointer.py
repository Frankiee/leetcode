# [Classic]
# https://leetcode.com/problems/copy-list-with-random-pointer/
# 138. Copy List with Random Pointer

# History:
# Facebook
# 1.
# Dec 8, 2019
# 2.
# Mar 27, 2020
# 3.
# Apr 1, 2020
# 4.
# May 8, 2020

# A linked list is given such that each node contains an additional random pointer which could
# point to any node in the list or null.
#
# Return a deep copy of the list.
#
# Example 1:
#
# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},
# "val":1}
#
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
#
#
# Note:
#
# You must return the copy of the given head as a reference to the cloned list.


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        origin_node = head

        while origin_node:
            clone = Node(origin_node.val)
            clone.next = origin_node.next
            origin_node.next = clone

            origin_node = origin_node.next.next

        origin_node = head

        while origin_node:
            if origin_node.random:
                origin_node.next.random = origin_node.random.next

            origin_node = origin_node.next.next

        origin_node = head

        ret = curr_node = Node(0)

        while origin_node:
            curr_node.next = origin_node.next

            origin_node.next = origin_node.next.next

            curr_node = curr_node.next
            origin_node = origin_node.next

        return ret.next
