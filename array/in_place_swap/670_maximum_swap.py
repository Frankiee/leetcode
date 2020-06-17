# [In-Place-Swap, Classic]
# https://leetcode.com/problems/maximum-swap/
# 670. Maximum Swap

# History:
# Facebook
# 1.
# Mar 8, 2020
# 2.
# Apr 13, 2020
# 3.
# May 12, 2020

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued
# number. Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]


class SolutionCurrMax(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_lst = list(str(num))

        curr_max, curr_max_idx = 0, None
        candidate_min_idx, candidate_max_idx = None, None

        for i in range(len(num_lst) - 1, -1, -1):
            if int(num_lst[i]) > curr_max:
                curr_max = int(num_lst[i])
                curr_max_idx = i

            if curr_max > int(num_lst[i]):
                candidate_min_idx = i
                candidate_max_idx = curr_max_idx

        if candidate_min_idx is not None:
            num_lst[candidate_min_idx], num_lst[candidate_max_idx] = (
                num_lst[candidate_max_idx], num_lst[candidate_min_idx])

        return int("".join(num_lst))


class SolutionMath(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = list(str(num))
        for i in range(1, len(str_num)):
            if int(str_num[i]) > int(str_num[i - 1]):
                curr_max = float('-inf')
                curr_max_idx = None
                for k in range(i, len(str_num)):
                    if int(str_num[k]) >= curr_max:
                        curr_max_idx = k
                        curr_max = int(str_num[k])

                for j in range(curr_max_idx):
                    if int(str_num[j]) < int(str_num[curr_max_idx]):
                        str_num[curr_max_idx], str_num[j] = str_num[j], str_num[curr_max_idx]
                        return int("".join(str_num))

        return num


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [int(c) for c in str(num)]
        last_appear = {}

        for i in range(len(nums)):
            last_appear[nums[i]] = i

        for i in range(len(nums)):
            for larger_digit in range(9, nums[i], -1):
                if larger_digit in last_appear and last_appear[larger_digit] > i:
                    nums[i], nums[last_appear[larger_digit]] = (
                        nums[last_appear[larger_digit]], nums[i])

                    return int("".join([str(n) for n in nums]))

        return num
