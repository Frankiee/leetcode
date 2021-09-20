# [DFS-Stack]
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# 1305. All Elements in Two Binary Search Trees

# History:
# Facebook
# 1.
# May 30, 2020
# 2.
# Apr 11, 2021

# Given two binary search trees root1 and root2.
#
# Return a list containing all the integers from both trees sorted in ascending order.
#
#
#
# Example 1:
#
#
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:
#
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# Example 3:
#
# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# Example 4:
#
# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# Example 5:
#
#
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#
#
# Constraints:
#
# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        ret, root1_stack, root2_stack = [], [], []

        while True:
            while root1:
                root1_stack.append(root1)
                root1 = root1.left

            while root2:
                root2_stack.append(root2)
                root2 = root2.left

            if not root1_stack and not root2_stack:
                return ret

            if not root1_stack or (root1_stack and root2_stack and root2_stack[-1].val <= root1_stack[-1].val):
                nxt = root2_stack.pop()
                ret.append(nxt.val)
                root2 = nxt.right
            elif not root2_stack or (root1_stack and root2_stack and root1_stack[-1].val < root2_stack[-1].val):
                nxt = root1_stack.pop()
                ret.append(nxt.val)
                root1 = nxt.right

        return ret
