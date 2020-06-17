# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K

# History:
# Facebook
# 1.
# Aug 17, 2019
# 2.
# Nov 23, 2019
# 3.
# Apr 6, 2020
# 4.
# Apr 22, 2020
# 5.
# May 15, 2020

# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].


from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1
        ret = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            expected_prefix_sum = prefix_sum - k

            ret += prefix_sum_freq[expected_prefix_sum]

            prefix_sum_freq[prefix_sum] += 1

        return ret
