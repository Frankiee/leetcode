# [Classic]
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# 117. Populating Next Right Pointers in Each Node II

# History:
# Facebook
# 1.
# Mar 28, 2020
# 2.
# Apr 8, 2020
# 3.
# May 15, 2020

# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space
# for this problem.
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next
# pointer to point to its next right node, just like in Figure B. The serialized output is in
# level order as connected by the next pointers, with '#' signifying the end of each level.
#
#
# Constraints:
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

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
        start = root

        while start:
            nxt_start, curr, prev_to_connect = None, start, None

            while curr:
                if curr.left:
                    if prev_to_connect:
                        prev_to_connect.next = curr.left
                    prev_to_connect = curr.left

                    if not nxt_start:
                        nxt_start = curr.left

                if curr.right:
                    if prev_to_connect:
                        prev_to_connect.next = curr.right
                    prev_to_connect = curr.right

                    if not nxt_start:
                        nxt_start = curr.right

                curr = curr.next

            start = nxt_start

        return root
