# [Greedy]
# https://leetcode.com/problems/maximum-length-of-pair-chain/
# 646. Maximum Length of Pair Chain

# History:
# 1.
# Sep 15, 2019
# 2.
# Nov 23, 2019

# You are given n pairs of numbers. In every pair, the first number is
# always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if
# b < c. Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed.
# You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda p: p[1])

        ret = 0
        curr_pair = None
        for p in pairs:
            if not curr_pair or curr_pair[1] < p[0]:
                curr_pair = p
                ret += 1

        return ret
