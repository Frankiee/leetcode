# [Prefix-Sum]
# https://leetcode.com/problems/continuous-subarray-sum/
# 523. Continuous Subarray Sum

# History:
# Facebook
# 1.
# Dec 10, 2019
# 2.
# Feb 22, 2020
# 3.
# Apr 4, 2020

# Given a list of non-negative numbers and a target integer k, write a function to check if the
# array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is,
# sums up to n*k where n is also an integer.
#
# Example 1:
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
#
#
# Note:
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.


class Solution1(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        curr_sum = 0
        dp_remainder = {0: -1}

        for i in range(len(nums)):
            curr_sum += nums[i]

            key = curr_sum % k if k != 0 else curr_sum

            if key in dp_remainder:
                if i - dp_remainder[key] > 1:
                    return True
            else:
                dp_remainder[key] = i

        return False


class Solution2(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if k != 0:
            nums = [n % k for n in nums]

        first_remainder_idx = {0: -1}

        for i, n in enumerate(nums):
            if n in first_remainder_idx:
                if i - first_remainder_idx[n] >= 2:
                    return True
            else:
                first_remainder_idx[n] = i

        return False
