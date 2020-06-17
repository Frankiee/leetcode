# [Archive]
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# 653. Two Sum IV - Input is a BST

# History:
# Facebook
# 1.
# May 4, 2020

# Given a Binary Search Tree and a target number, return true if there exist two elements in the
# BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
# Example 2:
#
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionInorderRecruision(object):
    def _in_order(self, node, k, seen):
        if not node:
            return False

        if self._in_order(node.left, k, seen):
            return True

        expected = k - node.val
        if expected in seen:
            return True

        seen.add(node.val)
        return self._in_order(node.right, k, seen)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        seen = set()
        return self._in_order(root, k, seen)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionInorderIteration(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen = set()
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return False

            nxt = stack.pop(-1)
            expected = k - nxt.val
            if expected in seen:
                return True
            seen.add(nxt.val)

            root = nxt.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDeprecated(object):
    def _dfs(self, root, lst):
        if not root:
            return

        self._dfs(root.left, lst)
        lst.append(root.val)
        self._dfs(root.right, lst)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        lst = []
        self._dfs(root, lst)

        l, r = 0, len(lst) - 1

        while l < r:
            total = lst[l] + lst[r]

            if total == k:
                return True
            elif total > k:
                r -= 1
            else:
                l += 1

        return False
