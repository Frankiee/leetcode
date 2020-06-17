# [Classic]
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# 314. Binary Tree Vertical Order Traversal

# History:
# Facebook
# 1.
# Feb 22, 2020
# 2.
# Apr 22, 2020
# 3.
# May 10, 2020

# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to
# bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples 1:
#
# Input: [3,9,20,null,null,15,7]
#
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
#
# Output:
#
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Examples 2:
#
# Input: [3,9,8,4,0,1,7]
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#
# Output:
#
# [
#   [4],
#   [9],
#   [3,0,1],
#   [8],
#   [7]
# ]
# Examples 3:
#
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7
#     /\
#    /  \
#    5   2
#
# Output:
#
# [
#   [4],
#   [9,5],
#   [3,0,1],
#   [8,2],
#   [7]
# ]

from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))

        mp = defaultdict(list)
        while queue:
            nxt, x = queue.popleft()

            mp[x].append(nxt.val)

            if nxt.left:
                queue.append((nxt.left, x-1))
            if nxt.right:
                queue.append((nxt.right, x+1))

        ret = []
        x = min(mp.keys())
        while x in mp:
            ret.append(mp[x])
            x += 1

        return ret
