# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. Convert Sorted Array to Binary Search Tree

# History:
# Facebook
# 1.
# Mar 7, 2020
# 2.
# May 11, 2020

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
# of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _sorted_array_to_bst(self, nums, l, r):
        if r < l:
            return None

        m = (r + l) / 2

        left = self._sorted_array_to_bst(nums, l, m - 1)
        right = self._sorted_array_to_bst(nums, m + 1, r)

        return TreeNode(nums[m], left, right)

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sorted_array_to_bst(nums, 0, len(nums) - 1)
