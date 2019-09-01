# [DP-Array-Subarray]
# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray

# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = None
        max_so_far = float('-inf')

        for n in nums:
            max_so_far = max(max_so_far, n)

            if n == 0:
                current = None
            else:
                if not current:
                    current = (n, float('inf')) if n > 0 else (
                        float('-inf'), n)
                else:
                    if n > 0:
                        max_so_far = max(max_so_far, n * current[0])
                        current = (
                            max(current[0] * n, n), min(current[1] * n, n))
                    else:
                        max_so_far = max(max_so_far, n * current[1])
                        current = (
                            max(current[1] * n, n), min(current[0] * n, n))

        return max_so_far
