# https://leetcode.com/problems/unique-binary-search-trees/
# 96. Unique Binary Search Trees

# History:
# Google
# 1.
# Mar 14, 2020

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        for i in range(n + 1):
            if i == 0:
                dp[i] = 1
            if i == 1:
                dp[i] = 1
            else:
                for j in range(1, i + 1):
                    dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]
