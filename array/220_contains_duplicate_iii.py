# [Classic]
# https://leetcode.com/problems/contains-duplicate-iii/
# 220. Contains Duplicate III

# History:
# Apple
# 1.
# Mar 21, 2020

# Given an array of integers, find out whether there are two distinct indices i and j in the
# array such that the absolute difference between nums[i] and nums[j] is at most t and the
# absolute difference between i and j is at most k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        buckets = {}
        wide = t + 1

        for idx, n in enumerate(nums):
            if idx >= k + 1:
                buckets.pop(nums[idx - k - 1] / wide)

            bucket_idx = n / wide
            if bucket_idx in buckets:
                return True
            if bucket_idx - 1 in buckets and abs(buckets[bucket_idx - 1] - n) <= t:
                return True
            if bucket_idx + 1 in buckets and abs(buckets[bucket_idx + 1] - n) <= t:
                return True

            buckets[bucket_idx] = n

        return False
