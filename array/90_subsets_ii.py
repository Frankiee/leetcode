# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II

# History:
# 1.
# Mar 16, 2019
# 2.
# Apr 6, 2020

# Given a collection of integers that might contain duplicates, nums,
# return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class SolutionRecursion(object):
    def _dfs(self, nums, i, ret, curr, used):
        if i == len(nums):
            ret.append(curr)
            return

        if i == 0 or nums[i] != nums[i-1] or used[i-1]:
            used[i] = True
            self._dfs(nums, i+1, ret, curr + [nums[i]], used)
            used[i] = False
        self._dfs(nums, i+1, ret, curr, used)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = [False] * len(nums)
        ret = []
        self._dfs(nums, 0, ret, [], used)
        return ret


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums = sorted(nums)
        ret, cur_added = [[]], []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                cur_added = [r[:] + [nums[i]] for r in cur_added]
            else:
                cur_added = [r[:] + [nums[i]] for r in ret]

            ret.extend(cur_added)

        return ret
