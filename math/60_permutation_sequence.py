# [Classic]
# https://leetcode.com/problems/permutation-sequence/
# 60. Permutation Sequence

# History:
# Facebook
# 1.
# May 6, 2020

# https://leetcode.com/problems/permutation-sequence/discuss/22597/Does-anyone-have-a-better-idea-Share-my-accepted-python-code-here

# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        divisor = 1
        for i in range(1, n):
            divisor *= i

        digits = [str(i) for i in range(1, n + 1)]

        ret = ""
        while k > 0:
            idx = k / divisor
            k %= divisor

            if k > 0:
                ret += digits.pop(idx)
            else:
                ret += digits.pop(idx - 1)
                ret += "".join(digits[::-1])
                break

            divisor /= len(digits)

        return ret
