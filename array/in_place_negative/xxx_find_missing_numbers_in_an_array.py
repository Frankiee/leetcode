# [In-Place-Negative, Classic]
# http://www.dailyinterviewpro.com/view.php?email=tonylee80%40gmail.com&token=c05f177527b857a4cd97a9f9ef73d144&pid=116  # noqa
# Find Missing Numbers in an Array

# History:
# 1.
# Nov 1, 2019
# Daily Interview Pro

# Find Missing Numbers in an Array
#
# Given an array of integers of size n, where all elements are between 1 and n inclusive,
# find all of the elements of [1, n] that do not appear in the array. Some numbers may appear
# more than once.
#
# Example:
# Input: [4,5,2,6,8,2,1,5]
# Output: [3,7]
# class Solution(object):
#   def findDisappearedNumbers(self, nums):
#     # Fill this in.
#
# nums = [4, 6, 2, 6, 7, 2, 1]
# print(Solution().findDisappearedNumbers(nums))
# # [3, 5]
#
# For this problem, you can assume that you can mutate the input array.


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i + 1)

        return ret


nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
