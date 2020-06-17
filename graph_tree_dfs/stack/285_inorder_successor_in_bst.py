# [DFS-Stack, Classic]
# https://leetcode.com/problems/inorder-successor-in-bst/
# 285. Inorder Successor in BST

# History:
# Facebook
# 1.
# Apr 5, 2020
# 2.
# Apr 23, 2020

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of
# TreeNode type.
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
#
#
# Note:
#
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
# Accepted


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionStack(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ret_next = False
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return None

            nxt = stack.pop(-1)

            if ret_next:
                return nxt

            if nxt == p:
                ret_next = True

            root = nxt.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionHelper(object):
    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        self.stack = []
        self._push_all_left(root)
        is_next = False

        while self.stack:
            nxt = self.stack.pop(-1)

            if is_next:
                return nxt

            if nxt == p:
                is_next = True

            self._push_all_left(nxt.right)
