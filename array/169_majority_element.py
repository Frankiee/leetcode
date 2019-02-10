# https://leetcode.com/problems/majority-element/description/
# 169. Majority Element

# Given an array of size n, find the majority element. The majority element
# is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_so_far = nums[0]
        majority_count = 0

        for n in nums:
            if n == majority_so_far:
                majority_count += 1
            elif majority_count > 0:
                majority_count -= 1
            else:
                majority_so_far = n
                majority_count = 1

        return majority_so_far
