# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# 926. Flip String to Monotone Increasing

# A string of '0's and '1's is monotone increasing if it consists of some
# number of '0's (possibly 0), followed by some number of '1's (also
# possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1'
# or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
#
#
# Example 1:
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
# Note:
#
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        step_0 = None
        step_1 = None

        for idx in range(len(S)):
            if S[idx] == '0':
                if idx > 0:
                    step_0, step_1 = step_0, min(step_0 + 1, step_1 + 1)
                else:
                    step_0, step_1 = 0, 1
            else:
                if idx > 0:
                    step_0, step_1 = step_0 + 1, min(step_0, step_1)
                else:
                    step_0, step_1 = 1, 0

        return min(step_0, step_1)
