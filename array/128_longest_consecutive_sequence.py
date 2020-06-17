# [Classic]
# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 128. Longest Consecutive Sequence

# History:
# 1.
# Feb 19, 2019
# 2.
# Nov 23, 2019
# 3.
# Mar 4, 2020
# 4.
# Apr 28, 2020

# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3,
# 4]. Therefore its length is 4.


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        ret = 0
        for n in nums:
            if n - 1 in nums:
                continue

            curr_num = n
            while curr_num in nums:
                curr_num += 1

            ret = max(ret, curr_num - n)

        return ret


class SolutionDict(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        mp = {}

        for n in nums:
            if n not in mp:
                seq = 1
                if n + 1 in mp:
                    seq += mp[n + 1]
                if n - 1 in mp:
                    seq += mp[n - 1]

                if n + 1 in mp:
                    mp[n + mp[n + 1]] = seq
                if n - 1 in mp:
                    mp[n - mp[n - 1]] = seq

                mp[n] = seq
                ret = max(ret, seq)

        return ret
