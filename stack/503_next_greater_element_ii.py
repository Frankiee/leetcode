# https://leetcode.com/problems/next-greater-element-ii/
# 503. Next Greater Element II

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# May 20, 2020

# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element.
# The Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search
# circularly to find its next greater number. If it doesn't exist, output -1
# for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is
# also 2.
# Note: The length of given array won't exceed 10000.


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [-1] * len(nums)

        stack = []
        for i, n in (list(enumerate(nums)) * 2):
            while stack and nums[stack[-1]] < n:
                idx = stack.pop(-1)
                ret[idx] = n
            stack.append(i)

        return ret
