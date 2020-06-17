# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# 865. Smallest Subtree with all the Deepest Nodes

# History:
# Facebook
# 1.
# Jan 3, 2020
# 2.
# Apr 1, 2020
# 3.
# Apr 12, 2020
# 4.
# May 2, 2020

# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
#
# A node is deepest if it has the largest depth possible among any node in the entire tree.
#
# The subtree of a node is that node, plus the set of all descendants of that node.
#
# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.
#
#
#
# Example 1:
#
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
#
#
#
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
# Both the input and output have TreeNode type.
#
#
# Note:
#
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def subtree_depth_node(self, node):
        if not node:
            return 0, None

        left_depth, left_node = self.subtree_depth_node(node.left)
        right_depth, right_node = self.subtree_depth_node(node.right)

        if left_depth == right_depth:
            return left_depth + 1, node
        elif left_depth < right_depth:
            return right_depth + 1, right_node
        else:
            return left_depth + 1, left_node

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        _, node = self.subtree_depth_node(root)

        return node
