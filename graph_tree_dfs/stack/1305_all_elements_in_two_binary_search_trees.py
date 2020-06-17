# [DFS-Stack]
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# 1305. All Elements in Two Binary Search Trees

# History:
# Facebook
# 1.
# May 30, 2020

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
        ret = []
        tree1_stack, tree2_stack = [], []

        while True:
            while root1:
                tree1_stack.append(root1)
                root1 = root1.left
            while root2:
                tree2_stack.append(root2)
                root2 = root2.left

            if tree1_stack and tree2_stack:
                if tree1_stack[-1].val <= tree2_stack[-1].val:
                    root1 = tree1_stack.pop(-1)
                    ret.append(root1.val)

                    root1 = root1.right
                else:
                    root2 = tree2_stack.pop(-1)
                    ret.append(root2.val)

                    root2 = root2.right
            elif tree1_stack:
                root1 = tree1_stack.pop(-1)
                ret.append(root1.val)

                root1 = root1.right
            elif tree2_stack:
                root2 = tree2_stack.pop(-1)
                ret.append(root2.val)

                root2 = root2.right
            else:
                return ret
