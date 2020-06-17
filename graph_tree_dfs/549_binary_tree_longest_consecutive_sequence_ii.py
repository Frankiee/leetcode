# [Classic]
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# 549. Binary Tree Longest Consecutive Sequence II

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# May 12, 2020

# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
#
# Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,
# 2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand,
# the path can be in the child-Parent-child order, where not necessarily be parent-child order.
#
# Example 1:
#
# Input:
#         1
#        / \
#       2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
#
#
# Example 2:
#
# Input:
#         2
#        / \
#       1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
#
#
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, node):
        if not node:
            return 0, 0, 0

        left_longest, left_through_incre, left_through_decre = self._dfs(node.left)
        right_longest, right_through_incre, right_through_decre = self._dfs(node.right)

        longest = max(left_longest, right_longest, 1)
        through_incre = through_decre = 1

        if node.left and node.right:
            if node.left.val + 1 == node.val == node.right.val - 1:
                longest = max(longest, left_through_incre + 1 + right_through_decre)
            elif node.left.val - 1 == node.val == node.right.val + 1:
                longest = max(longest, left_through_decre + 1 + right_through_incre)

        if node.left:
            if node.left.val + 1 == node.val:
                longest = max(longest, 1 + left_through_incre)
                through_incre = 1 + left_through_incre
            elif node.left.val - 1 == node.val:
                longest = max(longest, 1 + left_through_decre)
                through_decre = 1 + left_through_decre

        if node.right:
            if node.right.val + 1 == node.val:
                longest = max(longest, 1 + right_through_incre)
                through_incre = max(through_incre, 1 + right_through_incre)
            elif node.right.val - 1 == node.val:
                longest = max(longest, 1 + right_through_decre)
                through_decre = max(through_decre, 1 + right_through_decre)

        return longest, through_incre, through_decre

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, _, _ = self._dfs(root)

        return ret
