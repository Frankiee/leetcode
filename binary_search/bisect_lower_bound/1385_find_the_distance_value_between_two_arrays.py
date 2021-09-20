# [Bisect-Lower-Bound]
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# 1385. Find the Distance Value Between Two Arrays

# History:
# 1.
# Sep 18, 2021

# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
#
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where
# |arr1[i]-arr2[j]| <= d.
#
#
#
# Example 1:
#
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation:
# For arr1[0]=4 we have:
# |4-10|=6 > d=2
# |4-9|=5 > d=2
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# For arr1[1]=5 we have:
# |5-10|=5 > d=2
# |5-9|=4 > d=2
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
# Example 2:
#
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2
# Example 3:
#
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1
#
#
# Constraints:
#
# 1 <= arr1.length, arr2.length <= 500
# -10^3 <= arr1[i], arr2[j] <= 10^3
# 0 <= d <= 100

class Solution(object):
    def _bisect(self, val, arr1):
        l, r = 0, len(arr1)

        while l < r:
            m = (r - l) / 2 + l

            if arr1[m] >= val:
                r = m
            else:
                l = m + 1

        return l

    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()

        ret = 0
        for v in arr1:
            i = self._bisect(v, arr2)
            if not (i < len(arr2) and abs(v - arr2[i]) <= d or i - 1 >= 0 and abs(v - arr2[i - 1]) <= d):
                ret += 1

        return ret
