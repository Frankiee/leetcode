# [Classic]
# https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 6, 2020
# 3.
# Apr 22, 2020
# 4.
# May 12, 2020

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is
# equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra
# space for the purpose of space complexity analysis.)


class SolutionInPlace(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        non_zero_product = 1
        zero_count = 0

        for n in nums:
            if n != 0:
                non_zero_product *= n
            else:
                zero_count += 1

        ret = []

        for n in nums:
            if zero_count >= 2:
                ret.append(0)
            elif zero_count == 0:
                ret.append(non_zero_product / n)
            else:
                ret.append(0 if n != 0 else non_zero_product)

        return ret


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [1] * len(nums)

        curr_p = 1
        for i in range(1, len(nums)):
            curr_p *= nums[i - 1]
            ret[i] = curr_p

        curr_p = 1
        for i in range(len(nums) - 2, -1, -1):
            curr_p *= nums[i + 1]
            ret[i] *= curr_p

        return ret
