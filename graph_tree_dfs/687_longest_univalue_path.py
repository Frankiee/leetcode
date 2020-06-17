# https://leetcode.com/problems/longest-univalue-path/
# 687. Longest Univalue Path

# History:
# Facebook
# 1.
# Mar 19, 2020

# Given a binary tree, find the length of the longest path where each node in the path has the
# same value. This path may or may not pass through the root.
#
# The length of path between two nodes is represented by the number of edges between them.
#
#
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
#
#
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
#
#
#
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more
# than 1000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _dfs(self, node):
        if not node:
            return 0, 0

        left_max, left_max_through = self._dfs(node.left)
        right_max, right_max_through = self._dfs(node.right)

        curr_max = through_max = 0
        if node.left and node.right and node.val == node.left.val == node.right.val:
            curr_max = left_max_through + 2 + right_max_through
            through_max = max(left_max_through + 1, right_max_through + 1)
        elif node.left and node.left.val == node.val:
            curr_max = left_max_through + 1
            through_max = left_max_through + 1
        elif node.right and node.right.val == node.val:
            curr_max = right_max_through + 1
            through_max = right_max_through + 1

        return max(left_max, right_max, curr_max), through_max

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_max, _ = self._dfs(root)

        return curr_max
