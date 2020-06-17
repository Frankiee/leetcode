# [DFS-Stack]
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# 94. Binary Tree Inorder Traversal

# History:
# Google, Facebook
# 1.
# Mar 14, 2020
# 2.
# May 12, 2020

# Given a binary tree, return the inorder traversal of its nodes' values.
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
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x31
#         self.left = None
#         self.right = None

class SolutionStack(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return ret

            nxt = stack.pop()
            ret.append(nxt.val)
            root = nxt.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionRecrusion(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        left.append(root.val)
        left.extend(self.inorderTraversal(root.right))

        return left
