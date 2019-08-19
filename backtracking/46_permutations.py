# [Important]
# https://leetcode.com/problems/permutations/
# 46. Permutations

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# Iteration
class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]

        for n in nums:
            next_ret = []
            for r in ret:
                for insert_point in range(len(r) + 1):
                    next_ret.append(r[:insert_point] + [n] + r[insert_point:])

            ret = next_ret

        return ret


# Recursion
class Solution2(object):
    def dfs(self, ret, nums, used, prefix):
        if len(prefix) == len(nums):
            ret.append(prefix)
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                self.dfs(ret, nums, used, prefix + [nums[i]])
                used[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False] * len(nums)
        ret = []

        self.dfs(ret, nums, used, [])

        return ret
