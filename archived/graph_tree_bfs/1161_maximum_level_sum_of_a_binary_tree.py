# [Archived]
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# 1161. Maximum Level Sum of a Binary Tree

# Given the root of a binary tree, the level of its root is 1, the level of
# its children is 2, and so on.
#
# Return the smallest level X such that the sum of all the values of nodes
# at level X is maximal.
#
#
# Example 1:
#
#
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
#
#
# Note:
#
# The number of nodes in the given tree is between 1 and 10^4.
# -10^5 <= node.val <= 10^5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        current_level = 1
        level_nodes = [root]
        max_level = None
        max_sum = float('-inf')

        while level_nodes:
            current_level_sum = 0
            next_level_nodes = []

            for n in level_nodes:
                current_level_sum += n.val
                if n.left:
                    next_level_nodes.append(n.left)
                if n.right:
                    next_level_nodes.append(n.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level

            current_level += 1
            level_nodes = next_level_nodes

        return max_level
