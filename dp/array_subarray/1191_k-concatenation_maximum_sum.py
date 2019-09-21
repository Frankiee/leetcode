# [DP-Array-Subarray]
# https://leetcode.com/problems/k-concatenation-maximum-sum/
# 1191. K-Concatenation Maximum Sum

# Given an integer array arr and an integer k, modify the array by repeating
# it k times.
#
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1,
# 2, 1, 2, 1, 2].
#
# Return the maximum sub-array sum in the modified array. Note that the
# length of the sub-array can be 0 and its sum in that case is 0.
#
# As the answer can be very large, return the answer modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: arr = [1,2], k = 3
# Output: 9
# Example 2:
#
# Input: arr = [1,-2,1], k = 5
# Output: 2
# Example 3:
#
# Input: arr = [-1,-2], k = 7
# Output: 0
#
#
# Constraints:
#
# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4


class Solution(object):
    def _max_array(self, arr):
        max_start_idx = max_end_idx = None

        curr_max = 0
        curr_sum = 0
        curr_positive_start_idx = None

        for idx in range(len(arr)):
            n = arr[idx]
            curr_sum = max(0, curr_sum + n)

            if curr_sum > 0 and max_start_idx is None:
                curr_positive_start_idx = idx
            elif curr_sum < 0:
                curr_positive_start_idx = None

            if curr_sum > curr_max:
                max_start_idx = curr_positive_start_idx
                max_end_idx = idx

            curr_max = max(curr_max, curr_sum)

        return max_start_idx, max_end_idx, curr_max

    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7

        if k == 1:
            return self._max_array(arr)[2] % mod
        if k == 2:
            return self._max_array(arr + arr)[2] % mod
        else:
            three_arr = arr * 3

            start_idx, end_idx, max_sum = self._max_array(three_arr)
            if not start_idx and not end_idx:
                return 0
            elif start_idx == 0 and end_idx == len(three_arr) - 1:
                return k * sum(arr) % mod
            elif start_idx < len(arr) and end_idx >= len(arr) * 2:
                return (max_sum + (k - 3) * sum(arr)) % mod
            else:
                return max_sum % mod
