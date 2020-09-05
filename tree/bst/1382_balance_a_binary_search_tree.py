# [BST]
# https://leetcode.com/problems/balance-a-binary-search-tree/
# 1382. Balance a Binary Search Tree

# History
# Google
# 1.
# July 30, 2020

# Given a binary search tree, return a balanced binary search tree with the same node values.
#
# A binary search tree is balanced if and only if the depth of the two subtrees of every node
# never differ by more than 1.
#
# If there is more than one answer, return any of them.
#
#
#
# Example 1:
#
#
#
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
#
#
# Constraints:
#
# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _bst_to_sorted_array(self, root, ret):
        if not root:
            return

        self._bst_to_sorted_array(root.left, ret)
        ret.append(root.val)
        self._bst_to_sorted_array(root.right, ret)

    def _sorted_array_to_node(self, arry, l, r):
        if l > r:
            return

        if l == r:
            return TreeNode(val=arry[r])

        m = (r - l) / 2 + l

        return TreeNode(
            val=arry[m],
            left=self._sorted_array_to_node(arry, l, m - 1),
            right=self._sorted_array_to_node(arry, m + 1, r)
        )

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ret = []
        self._bst_to_sorted_array(root, ret)

        return self._sorted_array_to_node(ret, 0, len(ret) - 1)
