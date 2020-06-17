# [Classic]
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# 116. Populating Next Right Pointers in Each Node

# History:
# Facebook
# 1.
# Aug 31, 2019
# 2.
# Nov 23, 2019
# 3.
# Mar 28, 2020
# 4.
# Apr 30, 2020

# You are given a perfect binary tree where all leaves are on the same
# level, and every parent has two children. The binary tree has the
# following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Example:
#
# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,
# "next":null,"right":null,"val":4},"next":null,"right":{"$id":"4",
# "left":null,"next":null,"right":null,"val":5},"val":2},"next":null,
# "right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,
# "val":6},"next":null,"right":{"$id":"7","left":null,"next":null,
# "right":null,"val":7},"val":3},"val":1}
#
# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,
# "next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{
# "$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,
# "val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7",
# "left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{
# "$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
#
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node,
# just like in Figure B.
#
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level_start = root

        while level_start:
            nxt_level_start = None
            curr = level_start

            while curr:
                if curr.left:
                    if nxt_level_start is None:
                        nxt_level_start = curr.left
                    curr.left.next = curr.right

                if curr.right:
                    if curr.next:
                        curr.right.next = curr.next.left

                curr = curr.next

            level_start = nxt_level_start

        return root


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class SolutionRecursionWithConstSpace(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)

        return root


class SolutionWithExtraSpace(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return

        last_level_left = root

        while last_level_left:
            last_current_node = last_level_left
            while last_current_node and last_current_node.left:
                current_node = last_current_node.left
                current_node.next = last_current_node.right
                current_node = last_current_node.right

                last_current_node = last_current_node.next
                current_node.next = (
                    last_current_node.left
                    if last_current_node else None
                )
            last_level_left = last_level_left.left

        return root
