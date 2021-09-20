# [Archive]
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# 637. Average of Levels in Binary Tree

# History:
# Facebook
# 1.
# Dec 20, 2019
# 2.
# Apr 11, 2020
# 3.
# May 2, 2020

# Given a non-empty binary tree, return the average value of the nodes on each level in the form
# of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence
# return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.


from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _dfs(self, node, level, count_mp, total_mp):
        if not node:
            return

        count_mp[level] += 1
        total_mp[level] += node.val

        self._dfs(node.left, level + 1, count_mp, total_mp)
        self._dfs(node.right, level + 1, count_mp, total_mp)

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        count_mp = defaultdict(int)
        total_mp = defaultdict(int)

        self._dfs(root, 0, count_mp, total_mp)

        level = 0
        ret = []

        while level in count_mp:
            ret.append(total_mp[level] / float(count_mp[level]))
            level += 1

        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []

        level = [root]

        while level:
            next_level = []

            ret.append(sum([n.val for n in level]) / float(len(level)))

            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            level = next_level

        return ret
