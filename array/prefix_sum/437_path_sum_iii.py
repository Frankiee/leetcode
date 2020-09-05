# [Classic, Prefix-Sum]
# https://leetcode.com/problems/path-sum-iii/
# 437. Path Sum III

# History:
# Facebook
# 1.
# Apr 24, 2020

# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (
# traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionGlobalVariable(object):
    def _dfs(self, node, sum, curr, prefix_sum):
        if not node:
            return

        curr += node.val
        expected = curr - sum
        self.ret += prefix_sum[expected]
        prefix_sum[curr] += 1

        self._dfs(node.left, sum, curr, prefix_sum)
        self._dfs(node.right, sum, curr, prefix_sum)

        prefix_sum[curr] -= 1

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.ret = 0

        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1
        self._dfs(root, sum, 0, prefix_sum)
        return self.ret


from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionReturnResult(object):
    def _dfs(self, node, sum, prefix_sum, prefix_sum_frequency):
        if not node:
            return 0

        prefix_sum += node.val
        expected = prefix_sum - sum

        ret = prefix_sum_frequency[expected]

        prefix_sum_frequency[prefix_sum] += 1
        ret += self._dfs(node.left, sum, prefix_sum, prefix_sum_frequency)
        ret += self._dfs(node.right, sum, prefix_sum, prefix_sum_frequency)
        prefix_sum_frequency[prefix_sum] -= 1

        return ret

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefix_sum_frequency = defaultdict(int)
        prefix_sum_frequency[0] += 1

        return self._dfs(root, sum, 0, prefix_sum_frequency)
