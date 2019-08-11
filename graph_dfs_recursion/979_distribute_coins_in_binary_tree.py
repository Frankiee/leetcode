# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# 979. Distribute Coins in Binary Tree

# Given the root of a binary tree with N nodes, each node in the tree has
# node.val coins, and there are N coins total.
#
# In one move, we may choose two adjacent nodes and move one coin from one
# node to another.  (The move may be from parent to child, or from child to
# parent.)
#
# Return the number of moves required to make every node have exactly one coin.
#
#
# Example 1:
#
#
# Input: [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left
# child, and one coin to its right child.
#
# Example 2:
#
#
# Input: [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the
# root [taking two moves].  Then, we move one coin from the root of the tree
# to the right child.
#
# Example 3:
#
#
# Input: [1,0,2]
# Output: 2
#
# Example 4:
#
#
# Input: [1,0,0,null,3]
# Output: 4
#
#
# Note:
#
# 1<= N <= 100
# 0 <= node.val <= N


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distribute_coins(self, root):
        if not root:
            return 0, 0
        if not root.left and not root.right:
            return root.val - 1, abs(root.val - 1)

        left_flow, left_steps = self.distribute_coins(root.left)
        right_flow, right_steps = self.distribute_coins(root.right)

        return left_flow + right_flow + root.val - 1, abs(left_steps) + abs(
            right_steps) + abs(left_flow + right_flow + root.val - 1)

    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, steps = self.distribute_coins(root)

        return steps
