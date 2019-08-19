# [Important]
# https://leetcode.com/problems/largest-divisible-subset/description/
# 368. Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset such
# that every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]

# Explaination:
# https://leetcode.com/problems/largest-divisible-subset/discuss/83998/
# C++-Solution-with-Explanations

# The key concept here is:
# Given a set of integers that satisfies the property that each pair of
# integers inside the set are mutually divisible, for a new integer S,
# S can be placed into the set as long as it can divide the smallest number
# of the set or is divisible by the largest number of the set.
#
# For example, let's say we have a set P = { 4, 8, 16 }, P satisfies the
# divisible condition. Now consider a new number 2, it can divide the
# smallest number 4, so it can be placed into the set; similarly, 32 can be
# divided by 16, the biggest number in P, it can also placed into P.
#
# Next, let's define:
#
# EDIT: For clarification, the following definitions try to enlarge
# candidate solutions by appending a larger element at the end of each
# potential set, while my implementation below is prefixing a smaller
# element at the front of a set. Conceptually they are equivalent but by
# adding smaller elements at the front saves the trouble for keeping the
# correct increasing order for the final answer. Please refer to comments in
# code for more details.
#
# For an increasingly sorted array of integers a[1 .. n]
#
# T[n] = the length of the largest divisible subset whose largest number is
# a[n]
#
# T[n+1] = max{ 1 + T[i] if a[n+1] mod a[i] == 0 else 1 }
#
# Now, deducting T[n] becomes straight forward with a DP trick. For the
# final result we will need to maintain a backtrace array for the answer.


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)

        largest_subset_idx = None
        largest_subset_length = 0
        subset_length = [None] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                subset_length[i] = (1, None)
            else:
                largest = 1
                for p in range(i):
                    if nums[i] % nums[p] == 0:
                        if not subset_length[i] or (
                                subset_length[i][0] <= subset_length[p][0]):
                            subset_length[i] = (subset_length[p][0] + 1, p)
                if not subset_length[i]:
                    subset_length[i] = (1, None)

            if not largest_subset_idx or subset_length[i][
                0] > largest_subset_length:
                largest_subset_length = subset_length[i][0]
                largest_subset_idx = i

        ret = []
        while largest_subset_idx is not None:
            ret.insert(0, nums[largest_subset_idx])
            largest_subset_idx = subset_length[largest_subset_idx][1]

        return ret
