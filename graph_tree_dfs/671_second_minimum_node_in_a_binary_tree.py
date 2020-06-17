# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# 671. Second Minimum Node In a Binary Tree

# History:
# 1.
# Sep 2, 2019
# 2.
# Nov 23, 2019

# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property
# root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in
# the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
#
# Input:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
#
# Example 2:
#
# Input:
#     2
#    / \
#   2   2
#
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        if not root.left and not root.right:
            return -1

        left_second_smallest = self.findSecondMinimumValue(root.left)
        right_second_smallest = self.findSecondMinimumValue(root.right)

        ret = sorted([i for i in {
            left_second_smallest,
            right_second_smallest,
            root.left.val,
            root.right.val,
        } if i != -1])

        return ret[1] if len(ret) > 1 else -1
