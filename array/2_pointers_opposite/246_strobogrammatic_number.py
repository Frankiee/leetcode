# [2-Pointers-Opposite]
# https://leetcode.com/problems/strobogrammatic-number/
# 246. Strobogrammatic Number

# History:
# Facebook
# 1.
# Jan 30, 2020
# 2.
# May 6, 2020

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at
# upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a
# string.
#
# Example 1:
#
# Input:  "69"
# Output: true
# Example 2:
#
# Input:  "88"
# Output: true
# Example 3:
#
# Input:  "962"
# Output: false


class Solution(object):
    ROTATABLE_NUM = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6',
    }

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r = 0, len(num) - 1

        while l <= r:
            if self.ROTATABLE_NUM.get(num[l]) != num[r]:
                return False

            l += 1
            r -= 1

        return True
