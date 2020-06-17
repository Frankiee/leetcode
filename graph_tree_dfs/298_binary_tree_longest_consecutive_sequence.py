# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
# 298. Binary Tree Longest Consecutive Sequence

# History:
# Facebook
# 1.
# Mar 15, 2020

# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along
# the parent-child connections. The longest consecutive path need to be from parent to child (
# cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _longest_consecutive(self, root):
        if not root:
            return 0, 0

        if not root.left and not root.right:
            return 1, 1

        left_max, left_through_max = self._longest_consecutive(root.left)
        right_max, right_through_max = self._longest_consecutive(root.right)

        max_through = 1
        if left_max and root.val == root.left.val - 1:
            max_through = max(max_through, left_through_max + 1)
        if right_max and root.val == root.right.val - 1:
            max_through = max(max_through, right_through_max + 1)

        return max(left_max, right_max, max_through), max_through

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_max, _ = self._longest_consecutive(root)
        return root_max
