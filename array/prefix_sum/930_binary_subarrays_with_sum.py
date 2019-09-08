# [Prefix-Sum]
# https://leetcode.com/problems/binary-subarrays-with-sum/
# 930. Binary Subarrays With Sum

# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
#
# Example 1:
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Note:
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.

from collections import Counter


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        ct = Counter({0: 1})

        ret = 0
        prefix_sum = 0
        for c in A:
            prefix_sum += c
            ret += ct[prefix_sum - S]
            ct[prefix_sum] += 1

        return ret
