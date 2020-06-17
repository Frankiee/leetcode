# [DP-Sequence-Action]
# https://leetcode.com/problems/delete-and-earn/
# 740. Delete and Earn

# History:
# Uber
# Dec 8, 2019

# https://www.youtube.com/watch?v=YzZd-bsMthk
# Related: 198. House Robber

# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i]
# points. After, you must delete every element equal to nums[i] - 1 or nums[
# i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn
# by applying such operations.
#
# Example 1:
#
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
#
#
# Example 2:
#
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
#
#
# Note:
#
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].


from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)

        values_total = sorted(
            [(v, f * v) for (v, f) in counter.items()],
            key=lambda i: i[0]
        )

        if len(values_total) == 0:
            return 0
        if len(values_total) == 1:
            return values_total[0][1]
        if len(values_total) == 2:
            if values_total[1][0] == values_total[0][0] + 1:
                return max(values_total[1][1], values_total[0][1])
            else:
                return values_total[1][1] + values_total[0][1]

        dp_minus_2 = values_total[0][1]
        if values_total[1][0] == values_total[0][0] + 1:
            dp_minus_1 = max(values_total[1][1], values_total[0][1])
        else:
            dp_minus_1 = values_total[1][1] + values_total[0][1]

        for i in range(2, len(values_total)):
            if values_total[i][0] == values_total[i - 1][0] + 1:
                dp_minus_2, dp_minus_1 = dp_minus_1, max(dp_minus_2 + values_total[i][1],
                                                         dp_minus_1)
            else:
                dp_minus_2, dp_minus_1 = dp_minus_1, dp_minus_1 + values_total[i][1]

        return dp_minus_1
