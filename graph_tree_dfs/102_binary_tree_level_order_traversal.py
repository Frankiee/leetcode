# https://leetcode.com/problems/binary-tree-level-order-traversal/
# 102. Binary Tree Level Order Traversal

# History:
# Apple, Facebook
# 1.
# Mar 21, 2020
# 2.
# Apr 28, 2020

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to
# right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFS(object):
    def _dfs(self, root, level, mp):
        if not root:
            return

        mp[level].append(root.val)

        self._dfs(root.left, level + 1, mp)
        self._dfs(root.right, level + 1, mp)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mp = defaultdict(list)

        self._dfs(root, 0, mp)

        ret = []

        level = 0
        while level in mp:
            ret.append(mp[level])
            level += 1

        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        to_do = [root]

        ret = []
        while to_do:
            nxt_to_do = []
            level = []

            for n in to_do:
                level.append(n.val)
                if n.left:
                    nxt_to_do.append(n.left)
                if n.right:
                    nxt_to_do.append(n.right)

            to_do = nxt_to_do
            ret.append(level)

        return ret
