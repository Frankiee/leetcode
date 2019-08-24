# https://leetcode.com/problems/contiguous-array/description/
# 525. Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of
# 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff_count = 0
        longest = 0
        diff_arry = [None] * (len(nums) + 1)
        diff_arry[0] = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                diff_count += 1
            else:
                diff_count -= 1
            diff_arry[i + 1] = diff_count

        earlest_map = {}

        current_longest = 0
        for i in range(len(nums) + 1):
            if diff_arry[i] not in earlest_map:
                earlest_map[diff_arry[i]] = i
            current_longest = max(current_longest,
                                  i - earlest_map[diff_arry[i]])

        return current_longest
