# [Archived]
# https://leetcode.com/problems/binary-tree-paths/
# 257. Binary Tree Paths

# History:
# Facebook
# 1.
# Dec 8, 2019
# 2.
# May 2, 2020

# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]

        left_path = self.binaryTreePaths(root.left)
        new_left_path = [str(root.val) + '->' + p for p in left_path]

        right_path = self.binaryTreePaths(root.right)
        new_right_path = [str(root.val) + '->' + p for p in right_path]

        return new_left_path + new_right_path


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def _dfs(self, root, curr, ret):
        if not root:
            return

        if not root.left and not root.right:
            curr.append(str(root.val))
            ret.append("->".join(curr))
            return

        self._dfs(root.left, curr + [str(root.val)], ret)
        self._dfs(root.right, curr + [str(root.val)], ret)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        self._dfs(root, [], ret)

        return ret
