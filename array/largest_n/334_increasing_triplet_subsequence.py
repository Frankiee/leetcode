# [Classic, Largest-N]
# https://leetcode.com/problems/increasing-triplet-subsequence/
# 334. Increasing Triplet Subsequence

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# May 4, 2020

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in
# the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: true
# Example 2:
#
# Input: [5,4,3,2,1]
# Output: false


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest, second = float('inf'), float('inf')

        for n in nums:
            smallest = min(smallest, n)
            if n > smallest:
                second = min(second, n)
            if n > second:
                return True

        return False
