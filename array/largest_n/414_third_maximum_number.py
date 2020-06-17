# https://leetcode.com/problems/third-maximum-number/
# 414. Third Maximum Number

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 6, 2020
# 3,
# Apr 13, 2020
# 4.
# May 8, 2020

# Given a non-empty array of integers, return the third maximum number in this array. If it does
# not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, second, third = float('-inf'), float('-inf'), float('-inf')

        for n in nums:
            if n in {first, second, third}:
                continue

            if n > first:
                first, second, third = n, first, second
            elif n > second:
                second, third = n, second
            elif n > third:
                third = n

        return third if third != float('-inf') else first
