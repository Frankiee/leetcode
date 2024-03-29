# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# 852. Peak Index in a Mountain Array

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# May 5, 2020

# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ...
# > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] <
# A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
# Input: [0,1,0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1
# Note:
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.


class Solution1(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A)

        while l < r:
            m = (r - l) / 2 + l

            if A[m] > A[m + 1] and A[m] > A[m - 1]:
                return m
            if A[m] > A[m + 1]:
                r = m
            else:
                l = m

        return l


class Solution2(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.insert(0, float('-inf'))
        A.append(float('-inf'))

        l, r = 0, len(A)

        while l < r:
            m = (r - l) / 2 + l

            if A[m] >= A[m + 1] and A[m] >= A[m - 1]:
                return m - 1
            elif A[m] >= A[m + 1]:
                r = m
            else:
                l = m + 1

        return l - 1
