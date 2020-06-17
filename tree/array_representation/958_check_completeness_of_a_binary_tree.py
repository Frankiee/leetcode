# [Array-Representation-Tree]
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# 958. Check Completeness of a Binary Tree

# History:
# Facebook
# 1.
# Dec 16, 2019
# 2.
# Apr 6, 2020
# 3,
# May 5, 2020

# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with
# node-values {1} and {2, 3}), and all nodes in the last level ({4, 5,
# 6}) are as far left as possible.
# Example 2:
#
#
#
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
# Note:
#
# The tree will have between 1 and 100 nodes.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionTreeArrayRepresentation(object):
    def _dfs(self, node, idx):
        if not node:
            return

        self.max_idx = max(self.max_idx, idx)
        self.count += 1

        self._dfs(node.left, idx * 2 + 1)
        self._dfs(node.right, idx * 2 + 2)

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.count = 0
        self.max_idx = 0

        self._dfs(root, 0)

        return self.count == self.max_idx + 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionDFS(object):
    def _is_complete_tree(self, root):
        if not root:
            return True, 0, 0

        left_complete, left_level_min, left_level_max = self._is_complete_tree(root.left)
        if not left_complete:
            return False, None, None

        right_complete, right_level_min, right_level_max = self._is_complete_tree(root.right)
        if not right_complete:
            return False, None, None

        if len({left_level_min, left_level_max, right_level_min, right_level_max}) > 2:
            return False, None, None

        if left_level_min < right_level_max:
            return False, None, None

        return (
            True,
            min(left_level_min, left_level_max, right_level_min, right_level_max) + 1,
            max(left_level_min, left_level_max, right_level_min, right_level_max) + 1
        )

    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        complete, _, _ = self._is_complete_tree(root)

        return complete


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        to_visit = [root]

        current_full = True
        while to_visit:
            next_to_visit = []
            for n in to_visit:
                if n.left:
                    if current_full == False:
                        return False
                    next_to_visit.append(n.left)
                else:
                    current_full = False
                if n.right:
                    if current_full == False:
                        return False
                    next_to_visit.append(n.right)
                else:
                    current_full = False

            to_visit = next_to_visit

        return True
