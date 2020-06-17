# [Stream, DFS-Stack, Classic]
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# 1008. Construct Binary Search Tree from Preorder Traversal

# History:
# Facebook
# 1.
# Jan 3, 2020

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionStream(object):
    def __init__(self):
        self.i = 0

    def bstFromPreorder(self, preorder, bound=float('inf')):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None

        root = TreeNode(preorder[self.i])
        self.i += 1

        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)

        return root


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
