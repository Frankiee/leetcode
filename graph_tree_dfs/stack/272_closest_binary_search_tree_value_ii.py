# [DFS-Stack]
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# 272. Closest Binary Search Tree Value II

# History:
# Facebook
# 1.
# Apr 23, 2020

# Given a non-empty binary search tree and a target value, find k values in the BST that are
# closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the
# target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: [4,3]
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total
# nodes)?


# Better solution exists
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        ret = deque()

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return ret

            nxt = stack.pop()

            ret.append(nxt.val)
            if len(ret) > k:
                if abs(ret[0] - target) > abs(ret[-1] - target):
                    ret.popleft()
                else:
                    ret.pop()
                    return ret

            root = nxt.right
