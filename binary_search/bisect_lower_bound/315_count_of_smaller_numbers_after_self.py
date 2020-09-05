# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 315. Count of Smaller Numbers After Self

# History:
# Google
# 1.
# Mar 13, 2020
# 2.
# Aug 1, 2020

# You are given an integer array nums and you have to return a new counts array. The counts array
# has the property where counts[i] is the number of smaller elements to the right of nums[i].
#
# Example:
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.


# Better solution exists using Merge Sort, Segment Tree
class Solution(object):
    def _bisect(self, nums, to_insert):
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] >= to_insert:
                r = m
            else:
                l = m + 1

        return l

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = [None] * len(nums)
        inserted = []
        for idx in range(len(nums) - 1, -1, -1):
            n = nums[idx]
            ist_pos = self._bisect(inserted, n)
            inserted.insert(ist_pos, n)
            ret[idx] = ist_pos

        return ret
