# https://leetcode.com/problems/combination-sum-ii/description/
# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
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
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]


class Solution(object):
    def dfs(self, candidates, remaining, start_index, path, ret):
        if remaining == 0:
            ret.append(path)
        elif remaining < 0:
            return
        else:
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                self.dfs(candidates, remaining - candidates[i], i + 1,
                         path + [candidates[i]], ret)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []

        candidates.sort()
        self.dfs(candidates, target, 0, [], ret)

        return ret
