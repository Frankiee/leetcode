# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/minimum-size-subarray-sum/
# 209. Minimum Size Subarray Sum

# History:
# Facebook
# 1.
# Jan 18, 2020
# 2.
# May 2, 2020

# Given an array of n positive integers and a positive integer s, find the minimal length of a
# contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time
# complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ret = float('inf')

        l = 0

        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum > s and l < r and curr_sum - nums[l] >= s:
                curr_sum -= nums[l]
                l += 1

            if curr_sum >= s:
                ret = min(ret, r - l + 1)
                if ret == 1:
                    return ret

        return ret if ret != float('inf') else 0
