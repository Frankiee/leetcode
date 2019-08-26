# [DpSequenceAction]
# https://leetcode.com/problems/delete-and-earn/
# 740. Delete and Earn

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
    def _get_house_robber_max(self, sorted_nums):
        if not sorted_nums:
            return 0
        if len(sorted_nums) == 1:
            return sorted_nums[0][1]

        # index 0 initially
        max_minus_2 = (sorted_nums[0][0], sorted_nums[0][1])
        # index 1 initially
        if max_minus_2[0] + 1 == sorted_nums[1][0]:
            max_minus_1 = (
            sorted_nums[1][0], max(max_minus_2[1], sorted_nums[1][1]))
        else:
            max_minus_1 = (
            sorted_nums[1][0], max_minus_2[1] + sorted_nums[1][1])

        for num, value in sorted_nums[2:]:
            if max_minus_1[0] + 1 == num:
                new_minus_1 = (
                num, max(max_minus_2[1] + value, max_minus_1[1]))
            else:
                new_minus_1 = (num, max_minus_1[1] + value)
            max_minus_1, max_minus_2 = new_minus_1, max_minus_1

        return max_minus_1[1]

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)

        sorted_nums = sorted(
            [(num, num * frequency) for num, frequency in counter.iteritems()],
            key=lambda (num, value): num,
        )

        return self._get_house_robber_max(sorted_nums)
