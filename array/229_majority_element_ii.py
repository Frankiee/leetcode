# [Boyer-Moore-Majority-Vote]
# https://leetcode.com/problems/majority-element-ii/
# 229. Majority Element II

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Mar 10, 2020

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        candidate1, candidate2, c1_count, c2_count = 1, 0, 0, 0

        for n in nums:
            if n == candidate1:
                c1_count += 1
            elif n == candidate2:
                c2_count += 1
            elif c1_count == 0:
                candidate1, c1_count = n, 1
            elif c2_count == 0:
                candidate2, c2_count = n, 1
            else:
                c1_count -= 1
                c2_count -= 1

        return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) / 3]
