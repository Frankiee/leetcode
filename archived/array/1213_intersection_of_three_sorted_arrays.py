# [Archived]
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
# 1213. Intersection of Three Sorted Arrays

# History:
# Facebook
# 1.
# Dec 8, 2019
# 2.
# Apr 29, 2020

# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a
# sorted array of only the integers that appeared in all three arrays.
#
#
#
# Example 1:
#
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
#
#
# Constraints:
#
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        ret = []

        arr1_pt = arr2_pt = arr3_pt = 0

        while arr1_pt < len(arr1) and arr2_pt < len(arr2) and arr3_pt < len(arr3):
            if arr1[arr1_pt] == arr2[arr2_pt] == arr3[arr3_pt]:
                ret.append(arr1[arr1_pt])
                arr1_pt += 1
                arr2_pt += 1
                arr3_pt += 1
            elif arr1[arr1_pt] <= arr2[arr2_pt] and arr1[arr1_pt] <= arr3[arr3_pt]:
                arr1_pt += 1
            elif arr2[arr2_pt] <= arr1[arr1_pt] and arr2[arr2_pt] <= arr3[arr3_pt]:
                arr2_pt += 1
            elif arr3[arr3_pt] <= arr1[arr1_pt] and arr3[arr3_pt] <= arr2[arr2_pt]:
                arr3_pt += 1

        return ret
