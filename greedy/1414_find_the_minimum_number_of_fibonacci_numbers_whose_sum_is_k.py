# [Greedy, Classic]
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

# History:
# Google
# 1.
# Jun 15, 2020

# Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k,
# whether a Fibonacci number could be used multiple times.
#
# The Fibonacci numbers are defined as:
#
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 , for n > 2.
# It is guaranteed that for the given constraints we can always find such fibonacci numbers that
# sum k.
#
#
# Example 1:
#
# Input: k = 7
# Output: 2
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
# For k = 7 we can use 2 + 5 = 7.
# Example 2:
#
# Input: k = 10
# Output: 2
# Explanation: For k = 10 we can use 2 + 8 = 10.
# Example 3:
#
# Input: k = 19
# Output: 3
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
#
#
# Constraints:
#
# 1 <= k <= 10^9


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 1

        fibonacci_nums = [1, 1]

        while fibonacci_nums[-1] + fibonacci_nums[-2] <= k:
            fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])

        ret = 0
        current_fibonacci_num_idx = len(fibonacci_nums) - 1

        while k > 0:
            ret += k / fibonacci_nums[current_fibonacci_num_idx]
            k %= fibonacci_nums[current_fibonacci_num_idx]
            current_fibonacci_num_idx -= 1

        return ret
