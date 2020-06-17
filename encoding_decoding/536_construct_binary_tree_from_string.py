# [Classic, Tree-Serialization-Deserialization]
# https://leetcode.com/problems/construct-binary-tree-from-string/
# 536. Construct Binary Tree from String

# History:
# Facebook
# 1.
# Apr 14, 2020

# You need to construct a binary tree from a string consisting of parenthesis and integers.
#
# The whole input represents a binary tree. It contains an integer followed by zero, one or two
# pairs of parenthesis. The integer represents the root's value and a pair of parenthesis
# contains a child binary tree with the same structure.
#
# You always start to construct the left child node of the parent first if it exists.
#
# Example:
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
# Note:
# There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def _str_2_tree(self, s, curr_idx):
        num = 0
        is_negative = False
        while curr_idx < len(s) and (s[curr_idx].isdigit() or s[curr_idx] == '-'):
            if s[curr_idx] == '-':
                is_negative = True
            else:
                num *= 10
                num += int(s[curr_idx])
            curr_idx += 1

        root = TreeNode(-num if is_negative else num)

        if curr_idx < len(s) and s[curr_idx] == '(':
            curr_idx += 1
            left_node, curr_idx = self._str_2_tree(s, curr_idx)
            curr_idx += 1
        else:
            left_node = None

        if curr_idx < len(s) and s[curr_idx] == '(':
            curr_idx += 1
            right_node, curr_idx = self._str_2_tree(s, curr_idx)
            curr_idx += 1
        else:
            right_node = None

        root.left = left_node
        root.right = right_node

        return root, curr_idx

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return None

        root, _ = self._str_2_tree(s, 0)

        return root
