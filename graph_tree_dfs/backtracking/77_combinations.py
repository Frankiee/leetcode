# [Backtracking, Classic]
# https://leetcode.com/problems/combinations/description/
# 77. Combinations

# History:
# 1.
# Feb 13, 2019
# 2.
# Oct 19, 2019
# 3.
# Nov 30, 2019
# 4.
# Apr 6, 2020

# Given two integers n and k, return all possible combinations of k numbers
# out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def dfs(self, n, k, start_digit, temp, ret):
        if k == 0:
            ret.append(temp)
            return

        for i in range(start_digit, n + 1):
            if n - i < k - 1:
                break
            self.dfs(n, k - 1, i + 1,  temp + [i], ret)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []

        self.dfs(n, k, 1, [], ret)

        return ret
