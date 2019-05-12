# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore
# the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?


# WARNING: Better solution exists
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_to_current = [1] * len(nums)
        ret = 1

        for i in range(len(nums)):
            if i == 0:
                max_to_current[0] = 1
                ret = max(ret, max_to_current[0])
            else:
                for j in range(i):
                    if nums[j] < nums[i]:
                        max_to_current[i] = max(
                            max_to_current[i],
                            max_to_current[j] + 1
                        )
                        ret = max(ret, max_to_current[i])

        return ret
