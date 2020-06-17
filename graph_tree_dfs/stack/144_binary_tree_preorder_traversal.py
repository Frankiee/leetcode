# [DFS-Stack]
# https://leetcode.com/problems/binary-tree-preorder-traversal/
# 144. Binary Tree Preorder Traversal

# History:
# Facebook
# 1.
# May 15, 2020

# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionPreorder(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack, ret = [root], []

        while stack:
            nxt = stack.pop(-1)

            ret.append(nxt.val)

            if nxt.right:
                stack.append(nxt.right)
            if nxt.left:
                stack.append(nxt.left)

        return ret


# Bonus: Postorder
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionPostOrder(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ret = deque()
        stack = [root]

        while stack:
            node = stack.pop()

            ret.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ret