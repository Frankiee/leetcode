# [Classic]
# https://leetcode.com/problems/binary-tree-postorder-traversal/
# 145. Binary Tree Postorder Traversal

# History:
# Facebook
# 1.
# May 6, 2020

# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?


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


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecursive(object):
    def _postorder_traversal(self, node, ret):
        if not node:
            return

        self._postorder_traversal(node.left, ret)
        self._postorder_traversal(node.right, ret)

        ret.append(node.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        self._postorder_traversal(root, ret)

        return ret


# Bonus: Preorder
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

