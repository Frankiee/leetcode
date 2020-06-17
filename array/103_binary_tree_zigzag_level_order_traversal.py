# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. Binary Tree Zigzag Level Order Traversal

# History:
# Facebook
# 1.
# Mar 11, 2020
# 2.
# May 24, 2020

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie,
# from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, root, level, mp):
        if not root:
            return

        if level % 2 == 0:
            mp[level].append(root.val)
        else:
            mp[level].appendleft(root.val)

        self._dfs(root.left, level + 1, mp)
        self._dfs(root.right, level + 1, mp)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        mp = defaultdict(deque)

        self._dfs(root, 0, mp)

        level = 0
        ret = []

        while level in mp:
            ret.append(mp[level])
            level += 1

        return ret


from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionBFS(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level = [root]
        order = True

        ret = []
        while level:
            ret.append(deque())
            nxt_level = []

            for n in level:
                if order:
                    ret[-1].append(n.val)
                else:
                    ret[-1].appendleft(n.val)

                if n.left:
                    nxt_level.append(n.left)
                if n.right:
                    nxt_level.append(n.right)

            level = nxt_level
            order = not order

        return ret
