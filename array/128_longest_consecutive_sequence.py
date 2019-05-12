# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 128. Longest Consecutive Sequence

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
        cache = {}
        max_length = 0
        for n in nums:
            if n in cache:
                continue

            lower_length, ll_idx = (
                cache.get(n - 1)
                if cache.get(n - 1) else
                (None, None)
            )
            higher_length, hh_idx = (
                cache.get(n + 1)
                if cache.get(n + 1) else
                (None, None)
            )

            if not lower_length and not higher_length:
                new_length = 1
                cache[n] = (new_length, n)
            elif lower_length and higher_length:
                new_length = lower_length + higher_length + 1
                cache[n] = (new_length, n)
                cache[ll_idx] = (new_length, hh_idx)
                cache[hh_idx] = (new_length, ll_idx)
            elif lower_length:
                new_length = lower_length + 1
                cache[n] = (new_length, ll_idx)
                cache[ll_idx] = (new_length, n)
            else:
                new_length = higher_length + 1
                cache[n] = (new_length, hh_idx)
                cache[hh_idx] = (new_length, n)

            max_length = max(max_length, new_length)

        return max_length
