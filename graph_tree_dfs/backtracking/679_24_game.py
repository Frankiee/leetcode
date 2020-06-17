# [Classic]
# https://leetcode.com/problems/24-game/
# 679. 24 Game

# History:
# Facebook
# 1.
# Mar 4, 2020
# 2.
# May 11, 2020

# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could
# operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 -
# 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary
# operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot
# write this as 12 + 12.


class Solution(object):
    def _dfs(self, nums):
        if len(nums) == 1:
            return abs(24 - nums[0]) < 0.001

        for i in range(len(nums)):
            n_i = nums.pop(i)
            for j in range(len(nums)):
                n_j = nums.pop(j)

                new_nums = [n_i + n_j, n_i - n_j, n_i * n_j]
                if n_j != 0:
                    new_nums.append(n_i / n_j)

                for new_num in new_nums:
                    if self._dfs(nums + [new_num]):
                        return True

                nums.insert(j, n_j)
            nums.insert(i, n_i)

        return False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float(n) for n in nums]

        return self._dfs(nums)
