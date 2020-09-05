# https://leetcode.com/problems/path-sum-ii/
# 113. Path Sum II

# History:
# Google
# 1.
# Jun 18, 2020

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the
# given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, node, sum, curr_path, ret):
        if not node:
            return

        if not node.left and not node.right:
            if sum == node.val:
                ret.append(curr_path + [node.val])
            return

        new_path = curr_path + [node.val]
        self._dfs(node.left, sum - node.val, new_path, ret)
        self._dfs(node.right, sum - node.val, new_path, ret)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self._dfs(root, sum, [], ret)

        return ret
