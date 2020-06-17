# [Backtracking, Classic]
# https://leetcode.com/problems/permutations/
# 46. Permutations

# History:
# Facebook
# 1.
# Aug 11, 2019
# 2.
# Oct 19, 2019
# 3.
# Nov 30, 2019
# 4.
# Apr 22, 2020

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


class SolutionRecursion(object):
    def _dfs(self, nums, i, ret):
        if i == len(nums):
            ret.append(nums[:])
            return

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self._dfs(nums, i + 1, ret)
            nums[i], nums[j] = nums[j], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self._dfs(nums, 0, ret)
        return ret


# Recursion
class SolutionRecursionLessEfficient(object):
    def _dfs(self, nums, used, curr_permu, ret):
        if len(curr_permu) == len(nums):
            ret.append(curr_permu)
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            self._dfs(nums, used, curr_permu + [nums[i]], ret)
            used[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False] * len(nums)
        ret = []
        self._dfs(nums, used, [], ret)
        return ret


# Iteration
class SolutionIteration(object):
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
