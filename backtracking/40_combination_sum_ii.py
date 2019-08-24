# https://leetcode.com/problems/combination-sum-ii/
# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


class Solution(object):
    def dfs(self, ret, candidates, start, target, used, prefix):
        if target < 0:
            return
        if target == 0:
            ret.append(prefix)

        for i in range(start, len(candidates)):
            if (i > 0 and candidates[i] == candidates[i - 1] and
                    not used[i - 1]):
                continue

            used[i] = True
            self.dfs(ret, candidates, i + 1, target - candidates[i], used,
                     prefix + [candidates[i]])
            used[i] = False

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = sorted(candidates)
        used = [False] * len(candidates)

        self.dfs(ret, candidates, 0, target, used, [])

        return ret
