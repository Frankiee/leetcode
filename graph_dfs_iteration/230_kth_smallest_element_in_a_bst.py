# [Important]
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# 230. Kth Smallest Element in a BST

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
        current_node = root
        current_k = 0

        while current_k < k:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            if not stack:
                return None

            current_node = stack.pop()
            current_k += 1

            if k == current_k:
                return current_node.val

            current_node = current_node.right

        return None
