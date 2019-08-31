# https://leetcode.com/problems/all-possible-full-binary-trees/
# 894. All Possible Full Binary Trees

# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
#
# Return a list of all possible full binary trees with N nodes.  Each
# element of the answer is the root node of one possible tree.
#
# Each node of each tree in the answer must have node.val = 0.
#
# You may return the final list of trees in any order.
#
# Example 1:
#
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,
# 0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
#
# Note:
#
# 1 <= N <= 20


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 0:
            return None

        dp = defaultdict(list)

        for n in range(1, N + 1, 2):
            if n == 1:
                dp[1].append(TreeNode(0))
            else:
                for left_c in range(1, N - 1, 2):
                    right_c = n - left_c - 1
                    for left_n in dp[left_c]:
                        for right_n in dp[right_c]:
                            r = TreeNode(0)
                            r.left = left_n
                            r.right = right_n
                            dp[n].append(r)

        return dp[N]
