# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# 1123. Lowest Common Ancestor of Deepest Leaves

# History:
# 1.
# Feb 4, 2020
# 2.
# Apr 9, 2020
# 3.
# May 2, 2020

# Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.
#
# Recall that:
#
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of
# its children is d+1.
# The lowest common ancestor of a set S of nodes is the node A with the largest depth such that
# every node in S is in the subtree with root A.
#
#
# Example 1:
#
# Input: root = [1,2,3]
# Output: [1,2,3]
# Explanation:
# The deepest leaves are the nodes with values 2 and 3.
# The lowest common ancestor of these leaves is the node with value 1.
# The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".
# Example 2:
#
# Input: root = [1,2,3,4]
# Output: [4]
# Example 3:
#
# Input: root = [1,2,3,4,5]
# Output: [2,4,5]
#
#
# Constraints:
#
# The given tree will have between 1 and 1000 nodes.
# Each node of the tree will have a distinct value between 1 and 1000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, node):
        if not node:
            return None, 0

        left_ret, left_depth = self._dfs(node.left)
        right_ret, right_depth = self._dfs(node.right)

        if left_depth == right_depth:
            return node, left_depth + 1
        elif left_depth > right_depth:
            return left_ret, left_depth + 1
        else:
            return right_ret, right_depth + 1

    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ret, _ = self._dfs(root)

        return ret
