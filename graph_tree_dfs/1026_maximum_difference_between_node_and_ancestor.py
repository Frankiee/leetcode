# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# 1026. Maximum Difference Between Node and Ancestor

# History:
# Facebook
# 1.
# Mar 4, 2020
# 2.
# Apr 28, 2020

# Given the root of a binary tree, find the maximum value V for which there exists different
# nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
#
# (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an
# ancestor of B.)
#
#
#
# Example 1:
#
#
#
# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation:
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
#
#
# Note:
#
# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def max_ancestor_diff(self, node):
        if not node:
            return 0, None, None

        left_ret, left_min, left_max = self.max_ancestor_diff(node.left)
        right_ret, right_min, right_max = self.max_ancestor_diff(node.right)

        curr_max, curr_min = node.val, node.val
        if right_min is not None:
            curr_min = min(curr_min, right_min)
            curr_max = max(curr_max, right_max)
        if left_min is not None:
            curr_min = min(curr_min, left_min)
            curr_max = max(curr_max, left_max)

        return max(
            left_ret, right_ret, abs(node.val - curr_min), abs(node.val - curr_max),
        ), curr_min, curr_max

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret, _, _ = self.max_ancestor_diff(root)
        return ret
