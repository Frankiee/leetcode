# https://leetcode.com/problems/shortest-distance-to-a-character/
# 821. Shortest Distance to a Character

# History:
# Apple
# 1.
# Mar 19, 2020

# Given a string S and a character C, return an array of integers representing the shortest
# distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
# Note:
#
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ret = [float('inf')] * len(S)

        distance = float('inf')
        for idx, c in enumerate(S):
            if c == C:
                distance = 0
            else:
                distance += 1

            ret[idx] = min(ret[idx], distance)

        distance = float('inf')
        for idx in range(len(S) - 1, -1, -1):
            c = S[idx]
            if c == C:
                distance = 0
            else:
                distance += 1

            ret[idx] = min(ret[idx], distance)

        return ret
