# [Backtracking]
# https://leetcode.com/problems/permutations-ii/
# 47. Permutations II

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
    def dfs(self, ret, nums, used, prefix):
        if len(prefix) == len(nums):
            ret.append(prefix)
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue

                used[i] = True
                self.dfs(ret, nums, used, prefix + [nums[i]])
                used[i] = False

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        used = [False] * len(nums)
        ret = []

        self.dfs(ret, nums, used, [])

        return ret
