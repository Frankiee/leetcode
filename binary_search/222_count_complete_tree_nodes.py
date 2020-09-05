# https://leetcode.com/problems/count-complete-tree-nodes/
# 222. Count Complete Tree Nodes

# History:
# Google
# 1.
# May 3, 2020
# 2.
# July 22, 2020

# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6


# Time: O(log(n)^2)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _get_left_height(self, node):
        height = 0

        while node:
            node = node.left
            height += 1

        return height

    def _get_right_height(self, node):
        height = 0

        while node:
            node = node.right
            height += 1

        return height

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_height = self._get_left_height(root)
        right_height = self._get_right_height(root)

        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionDeprecated(object):
    def _get_branch_status(self, node):
        if not node:
            return False, 0, 0

        r_has_ended, r_level_count, r_missing_count = self._get_branch_status(
            node.right)

        if r_has_ended:
            return r_has_ended, r_level_count + 1, r_missing_count

        l_has_ended, l_level_count, l_missing_count = self._get_branch_status(
            node.left)

        return r_has_ended or l_has_ended or r_level_count != l_level_count, max(
            l_level_count,
            r_level_count
        ) + 1, (
            r_missing_count + l_missing_count
            if r_level_count == l_level_count
            else l_missing_count + 2 ** (l_level_count - 1)
        )

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        _, level_count, missing_count = self._get_branch_status(root)

        return int((2 ** level_count - 1) - missing_count)
