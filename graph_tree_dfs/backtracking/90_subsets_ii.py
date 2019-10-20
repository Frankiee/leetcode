# [Backtracking, Classic]
# https://leetcode.com/problems/subsets-ii/
# 90. Subsets II

# History:
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019

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


# Iteration
class Solution1(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret, last_added = [[]], []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                last_added = [n + [nums[i]] for n in last_added]
            else:
                last_added = [n + [nums[i]] for n in ret]

            ret.extend(last_added)

        return ret


# Recursion
class Solution2(object):
    def dfs(self, ret, nums, start, prefix):
        ret.append(prefix)

        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue

            self.dfs(ret, nums, i + 1, prefix + [nums[i]])

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ret = []

        self.dfs(ret, nums, 0, [])

        return ret
