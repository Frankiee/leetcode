# https://leetcode.com/problems/boundary-of-binary-tree/
# 545. Boundary of Binary Tree

# History:
# Facebook
# 1.
# Mar 29, 2020

# Given a binary tree, return the values of its boundary in anti-clockwise direction starting
# from root. Boundary includes left boundary, leaves, and right boundary in order without
# duplicate nodes.  (The values of the nodes may still be duplicates.)
#
# Left boundary is defined as the path from root to the left-most node. Right boundary is defined
# as the path from root to the right-most node. If the root doesn't have left subtree or right
# subtree, then the root itself is left boundary or right boundary. Note this definition only
# applies to the input binary tree, and not applies to any subtrees.
#
# The left-most node is defined as a leaf node you could reach when you always firstly travel to
# the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf
# node.
#
# The right-most node is also defined by the same way with left and right exchanged.
#
# Example 1
#
# Input:
#   1
#    \
#     2
#    / \
#   3   4
#
# Ouput:
# [1, 3, 4, 2]
#
# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output
# reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
#
#
# Example 2
#
# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10
#
# Ouput:
# [1,2,4,7,8,9,10,6,3]
#
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _dfs_leaves(self, node, ret, root):
        if not node:
            return

        if not node.left and not node.right:
            if node != root:
                ret.append(node.val)
            return

        self._dfs_leaves(node.left, ret, root)
        self._dfs_leaves(node.right, ret, root)

    def _dfs_left_boundary(self, node, ret):
        if not node or (not node.left and not node.right):
            return

        ret.append(node.val)

        if node.left:
            self._dfs_left_boundary(node.left, ret)
        elif node.right:
            self._dfs_left_boundary(node.right, ret)

    def _dfs_right_boundary(self, node, ret):
        if not node or (not node.left and not node.right):
            return

        if node.right:
            self._dfs_right_boundary(node.right, ret)
        elif node.left:
            self._dfs_right_boundary(node.left, ret)

        ret.append(node.val)

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ret = [root.val]
        self._dfs_left_boundary(root.left, ret)
        self._dfs_leaves(root, ret, root)
        self._dfs_right_boundary(root.right, ret)

        return ret
