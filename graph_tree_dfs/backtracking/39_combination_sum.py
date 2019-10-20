# [Backtracking, Classic]
# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum

# History:
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019

# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where
# the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


class Solution(object):
    def dfs(self, ret, candidates, start, target, prefix):
        if target < 0:
            return
        if target == 0:
            ret.append(prefix)

        for i in range(start, len(candidates)):
            self.dfs(ret, candidates, i, target - candidates[i],
                     prefix + [candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []

        self.dfs(ret, candidates, 0, target, [])

        return ret
