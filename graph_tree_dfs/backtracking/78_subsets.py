# [Backtracking, Classic]
# https://leetcode.com/problems/subsets/
# 78. Subsets

# History:
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019

# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


# Iteration
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]

        for n in nums:
            current_added = [s + [n] for s in ret]
            ret.extend(current_added)

        return ret


# Recursion 1
import copy


class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        first = nums.pop(0)

        rest = self.subsets(nums)

        result = []

        for s in rest:
            result.append(s)
            s_copy = copy.copy(s)
            s_copy.append(first)
            result.append(s_copy)

        return result


# Recursion 2
class Solution2(object):
    def dfs(self, ret, nums, start, prefix):
        ret.append(prefix)

        for i in range(start, len(nums)):
            self.dfs(ret, nums, i + 1, prefix + [nums[i]])

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []

        self.dfs(ret, nums, 0, [])

        return ret
