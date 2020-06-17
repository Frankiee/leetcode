# [DP-Array-Subarray]
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# 674. Longest Continuous Increasing Subsequence

# History:
# Amazon
# 1.
# Dec 8, 2019
# 2.
# Apr 30, 3030

# Given an unsorted array of integers, find the length of longest continuous increasing
# subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and
# 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0

        curr = 0
        for i, n in enumerate(nums):
            if i == 0 or nums[i - 1] >= n:
                curr = 1
            else:
                curr += 1

            ret = max(ret, curr)

        return ret
