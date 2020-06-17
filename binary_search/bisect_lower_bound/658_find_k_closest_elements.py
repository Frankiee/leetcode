# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/find-k-closest-elements/
# 658. Find K Closest Elements

# History:
# Google
# 1.
# Mar 12, 2020
# 2.
# Apr 8, 2020
# 3.
# Apr 12, 2020
# 4.
# Apr 29, 2020

# Given a sorted array, two integers k and x, find the k closest elements to x in the array. The
# result should also be sorted in ascending order. If there is a tie, the smaller elements are
# always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers).
# Please reload the code definition to get the latest changes.


from collections import deque


class Solution(object):
    def _bisect(self, arr, x):
        l, r = 0, len(arr)

        while l < r:
            m = (r - l) / 2 + l

            if arr[m] >= x:
                r = m
            else:
                l = m + 1

        return l

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        pos = self._bisect(arr, x)

        l, r = pos - 1, pos

        ret = deque()
        while len(ret) < k:
            if 0 <= l < len(arr) and 0 <= r < len(arr):
                if x - arr[l] <= arr[r] - x:
                    ret.appendleft(arr[l])
                    l -= 1
                else:
                    ret.append(arr[r])
                    r += 1
            elif 0 <= l < len(arr):
                ret.appendleft(arr[l])
                l -= 1
            else:
                ret.append(arr[r])
                r += 1

        return ret
