# [Important]
# https://leetcode.com/problems/subarray-sum-equals-k/
# 560. Subarray Sum Equals K

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
        prefix_sum = defaultdict(int)

        ret = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum == k:
                ret += 1

            first = current_sum - k
            ret += prefix_sum.get(first) or 0

            prefix_sum[current_sum] += 1

        return ret
