# [Backtracking, Classic]
# https://leetcode.com/problems/permutations-ii/
# 47. Permutations II

# History:
# Amazon
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019
# 3.
# Nov 30, 2019
# 4.
# Mar 17, 2020
# 5.
# Apr 5, 2020
# 6.
# Apr 22, 2020

# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


# Recursion
class Solution(object):
    def dfs(self, nums, ret, prefix, used):
        if len(prefix) >= len(nums):
            ret.append(prefix)
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            self.dfs(nums, ret, prefix + [nums[i]], used)
            used[i] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        used = [False] * len(nums)

        nums.sort()
        self.dfs(nums, ret, [], used)

        return ret
