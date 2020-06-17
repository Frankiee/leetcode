# [Stream, Stack, Classic]
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# 1008. Construct Binary Search Tree from Preorder Traversal

# History:
# Facebook
# 1.
# Jan 3, 2020
# 2.
# May 4, 2020

# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of
# node.left has a value < node.val, and any descendant of node.right has a value > node.val.
# Also recall that a preorder traversal displays the value of the node first, then traverses
# node.left, then traverses node.right.)
#
#
#
# Example 1:
#
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#
#
#
# Note:
#
# 1 <= preorder.length <= 100
# The values of preorder are distinct.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _bst_from_preorder(self, preoder, upper_bounder=None):
        if self.i >= len(preoder) or (upper_bounder and preoder[self.i] > upper_bounder):
            return None

        root = TreeNode(preoder[self.i])
        self.i += 1

        root.left = self._bst_from_preorder(preoder, root.val)
        root.right = self._bst_from_preorder(preoder, upper_bounder)

        return root

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0
        return self._bst_from_preorder(preorder)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionStack(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for v in preorder[1:]:
            if stack and stack[-1].val > v:
                new_node = TreeNode(v)
                stack[-1].left = new_node
                stack.append(new_node)
            elif stack and stack[-1].val < v:
                while stack and stack[-1].val < v:
                    last_node = stack.pop()
                new_node = TreeNode(v)
                last_node.right = new_node
                stack.append(new_node)

        return root
