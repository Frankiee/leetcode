# [Archived]
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# 1304. Find N Unique Integers Sum up to Zero

# History:
# Facebook
# 1.
# May 29, 2020

# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
#
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
#
# Input: n = 1
# Output: [0]
#
#
# Constraints:
#
# 1 <= n <= 1000


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        if n % 2 == 1:
            ret.append(0)

        l, r = -1, 1
        n -= 1

        while n > 0:
            ret.append(l)
            ret.append(r)

            l -= 1
            r += 1
            n -= 2

        return ret
