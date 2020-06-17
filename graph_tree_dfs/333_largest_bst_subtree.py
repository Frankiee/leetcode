# [Classic]
# https://leetcode.com/problems/largest-bst-subtree/
# 333. Largest BST Subtree

# History:
# Facebook
# 1.
# May 5, 2020

# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
# where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
#
# Example:
#
# Input: [10,5,15,1,8,null,7]
#
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7
#
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, node):
        if not node:
            return True, 0, float('-inf'), float('inf')

        left_ret, left_count, left_max, left_min = self._dfs(node.left)
        right_ret, right_count, right_max, right_min = self._dfs(node.right)

        if not left_ret or not right_ret or node.val >= right_min or node.val <= left_max:
            return False, max(left_count, right_count), None, None

        return (
            True,
            left_count + right_count + 1,
            right_max if right_max != float('-inf') else node.val,
            left_min if left_min != float('inf') else node.val
        )

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, ret, _, _ = self._dfs(root)

        return ret
