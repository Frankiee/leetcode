# [Prefix-Sum]
# https://leetcode.com/problems/binary-subarrays-with-sum/
# 930. Binary Subarrays With Sum

# History:
# 1.
# Sep 8, 2019
# 2.
# Nov 20, 2019

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
        ret = 0
        counter = Counter({0: 1})
        prefix_sum = 0

        for n in A:
            prefix_sum += n
            ret += counter[prefix_sum - S]
            counter[prefix_sum] += 1

        return ret
