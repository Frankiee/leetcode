# [Backtracking, Classic]
# https://leetcode.com/problems/combination-sum/
# 39. Combination Sum

# History:
# Facebook
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019
# 3.
# Nov 30, 2019
# 4.
# Mar 8, 2020
# 5.
# Apr 6, 2020

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


class SolutionRecursion(object):
    def _dfs(self, candidates, target, idx, curr_ret, ret):
        if target == 0:
            ret.append(curr_ret)
            return
        if target < 0:
            return

        self._dfs(candidates, target - candidates[idx], idx, curr_ret + [candidates[idx]], ret)

        if idx < len(candidates) - 1:
            self._dfs(candidates, target, idx + 1, curr_ret, ret)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = sorted(candidates, reverse=True)

        self._dfs(candidates, target, 0, [], ret)

        return ret


class SolutionRecursion2(object):
    def _dfs(self, i, candidates, target_left, ret, curr_combo):
        if i == len(candidates):
            if target_left == 0:
                ret.append(curr_combo)
            return

        # take ith
        if target_left >= candidates[i]:
            self._dfs(i, candidates, target_left - candidates[i], ret, curr_combo + [candidates[i]])
        # do not take ith
        self._dfs(i + 1, candidates, target_left, ret, curr_combo)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        self._dfs(0, candidates, target, ret, [])
        return ret


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
