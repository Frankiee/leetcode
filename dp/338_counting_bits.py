# [Classic]
# https://leetcode.com/problems/counting-bits/
# 338. Counting Bits

# History:
# Facebook
# 1.
# Mar 18, 2020

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
# the number of 1's in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do
# it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in
# c++ or in any other language.


class SolutionDP(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)

        for i in range(1, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp


class SolutionDFS(object):
    def _dfs(self, curr_num, curr_bit_count, exp, ret, num):
        if curr_num > num or 2 ** (exp - 1) > num:
            return

        ret[curr_num] = curr_bit_count

        self._dfs(curr_num, curr_bit_count, exp + 1, ret, num)
        curr_num += 2 ** exp
        curr_bit_count += 1
        self._dfs(curr_num, curr_bit_count, exp + 1, ret, num)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0] * (num + 1)

        self._dfs(0, 0, 0, ret, num)

        return ret
