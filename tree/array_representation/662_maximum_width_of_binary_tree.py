# [Classic, Array-Representation-Tree]
# https://leetcode.com/problems/maximum-width-of-binary-tree/
# 662. Maximum Width of Binary Tree

# History:
# Facebook
# 1.
# Mar 27, 2020
# 2.
# Apr 30, 2020

# Given a binary tree, write a function to get the maximum width of the given tree. The width of
# a tree is the maximum width among all levels. The binary tree has the same structure as a full
# binary tree, but some nodes are null.
#
# The width of one level is defined as the length between the end-nodes (the leftmost and right
# most non-null nodes in the level, where the null nodes between the end-nodes are also counted
# into the length calculation.
#
# Example 1:
#
# Input:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:
#
# Input:
#
#           1
#          /
#         3
#        / \
#       5   3
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:
#
# Input:
#
#           1
#          / \
#         3   2
#        /
#       5
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:
#
# Input:
#
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,
# null,null,null,7).
#
#
# Note: Answer will in the range of 32-bit signed integer.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFS(object):
    def _dfs(self, node, x, y, mp):
        if not node:
            return 0

        ret = 1
        if y not in mp:
            mp[y] = x
        else:
            ret = x - mp[y] + 1

        ret = max(ret, self._dfs(node.left, 2 * x + 1, y + 1, mp))
        ret = max(ret, self._dfs(node.right, 2 * x + 2, y + 1, mp))

        return ret

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mp = {}
        return self._dfs(root, 0, 0, mp)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        to_do = [(root, 0)]

        ret = 0
        while to_do:
            next_to_do = []

            ret = max(ret, to_do[-1][1] - to_do[0][1] + 1)

            for node, val in to_do:
                if node.left:
                    next_to_do.append((node.left, (val << 1) + 1))
                if node.right:
                    next_to_do.append((node.right, (val << 1) + 2))

            to_do = next_to_do

        return ret
