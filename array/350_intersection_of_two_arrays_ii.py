# [Classic]
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 350. Intersection of Two Arrays II

# History:
# Facebook
# 1.
# Dec 9, 2019
# 2.
# Apr 12, 2020

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited
# such that you cannot load all elements into the memory at once?


from collections import Counter


class SolutionHash(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            num_to_hash = nums2
            num_to_loop = nums1
        else:
            num_to_hash = nums1
            num_to_loop = nums2

        counter = Counter(num_to_hash)

        ret = []
        for n in num_to_loop:
            if n in counter:
                ret.append(n)
                counter[n] -= 1

                if counter[n] == 0:
                    del counter[n]

        return ret


class SolutionTwoPointers(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()

        n1_p = n2_p = 0

        ret = []
        while n1_p < len(nums1) and n2_p < len(nums2):
            if nums1[n1_p] == nums2[n2_p]:
                ret.append(nums1[n1_p])
                n1_p += 1
                n2_p += 1
            elif nums1[n1_p] < nums2[n2_p]:
                n1_p += 1
            else:
                n2_p += 1

        return ret


class SolutionBinarySearch(object):
    def _bisect_left(self, nums, target, used):
        l, r = 0, len(nums)

        while l < r:
            m = (r - l) / 2 + l

            if nums[m] == target:
                if m not in used:
                    r = m
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m
            else:
                l = m + 1

        if l < len(nums) and nums[l] == target:
            return l

        return None

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            to_loop = nums2
            to_search = nums1
        else:
            to_loop = nums1
            to_search = nums2

        to_search.sort()

        ret = []
        used = set()
        for n in to_loop:
            p = self._bisect_left(to_search, n, used)
            if p is not None:
                ret.append(to_search[p])
                used.add(p)

        return ret
