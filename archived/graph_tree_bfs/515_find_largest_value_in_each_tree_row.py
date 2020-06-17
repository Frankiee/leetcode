# [Archived]
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# 515. Find Largest Value in Each Tree Row

# History:
# Facebook
# 1.
# Dec 14, 2019
# 2.
# Apr 30, 2020

# You need to find the largest value in each row of a binary tree.
#
# Example:
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFS(object):
    def _dfs(self, node, level, mp):
        if not node:
            return

        if level in mp:
            if node.val > mp[level]:
                mp[level] = node.val
        else:
            mp[level] = node.val

        self._dfs(node.left, level + 1, mp)
        self._dfs(node.right, level + 1, mp)

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mp = {}

        self._dfs(root, 0, mp)

        level = 0
        ret = []
        while level in mp:
            ret.append(mp[level])
            level += 1

        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None10601060
#         self.right = None

class SolutionBFS(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ret = []
        level = [root]

        while level:
            ret.append(max([n.val for n in level]))

            next_level = []
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            level = next_level

        return ret
