# [2-Pointers-Sliding-Window]
# https://leetcode.com/problems/max-consecutive-ones-iii/
# 1004. Max Consecutive Ones III

# History:
# Facebook
# 1.
# Mar 19, 2020
# 2.
# Apr 1, 2020
# 3.
# May 3, 2020

# History:
# Facebook
# 1.
# Jan 3, 2020

# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
#
# Return the length of the longest (contiguous) subarray that contains only 1s.
#
#
#
# Example 1:
#
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation:
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
# Example 2:
#
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation:
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
#
#
# Note:
#
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        remaining = K

        ret = 0
        l = 0
        for r in range(len(A)):
            if A[r] == 0:
                remaining -= 1

            while l <= r and remaining < 0:
                if A[l] == 0:
                    remaining += 1
                l += 1

            ret = max(ret, r - l + 1)

        return ret
