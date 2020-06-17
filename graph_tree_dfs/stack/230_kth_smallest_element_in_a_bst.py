# [DFS-Stack, Classic]
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230. Kth Smallest Element in a BST

# History:
# Apple
# 1.
# Jun 9, 2019
# 2.
# Mar 21, 2020
# 3.
# Apr 23, 2020
# 4.
# May 4, 2020

# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need
# to find the kth smallest frequently? How would you optimize the
# kthSmallest routine?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            nxt = stack.pop(-1)
            k -= 1

            if k == 0:
                return nxt.val

            root = nxt.right
