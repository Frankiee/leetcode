# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# 801. Minimum Swaps To Make Sequences Increasing

# https://www.youtube.com/watch?v=__yxFFRQAl8&t=614s

# History:
# Google
# 1.
# Aug 15, 2019
# 2.
# Mar 13, 2020

# We have two integer sequences A and B of the same non-zero length.
#
# We are allowed to swap elements A[i] and B[i].  Note that both elements
# are in the same index position in their respective sequences.
#
# At the end of some number of swaps, A and B are both strictly increasing.
# (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ...
# < A[A.length - 1].)
#
# Given A and B, return the minimum number of swaps to make both sequences
# strictly increasing.  It is guaranteed that the given input always makes
# it possible.
#
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation:
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
# Note:
#
# A, B are arrays with the same length, and that length will be in the range
# [1, 1000].
# A[i], B[i] are integer values in the range [0, 2000].


# DP
class Solution2(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        swap = [float('inf')] * len(A)
        keep = [float('inf')] * len(A)

        for i in range(len(A)):
            if i == 0:
                swap[i] = 1
                keep[i] = 0
            else:
                if A[i] > A[i - 1] and B[i] > B[i - 1]:
                    keep[i] = keep[i - 1]
                    swap[i] = swap[i - 1] + 1
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    keep[i] = min(keep[i], swap[i - 1])
                    swap[i] = min(swap[i], keep[i - 1] + 1)

        return min(keep[-1], swap[-1])


# DFS
class Solution1(object):
    def __init__(self):
        self.min_step = float('inf')

    def dfs(self, A, B, idx, current_step):
        if current_step >= self.min_step:
            return

        if idx >= len(A):
            self.min_step = min(current_step, self.min_step)
            return

        steps_1, steps_2 = float('inf'), float('inf')
        # Dont swap current index
        if idx == 0 or (A[idx] > A[idx - 1] and B[idx] > B[idx - 1]):
            self.dfs(A, B, idx + 1, current_step)

        # Swap current index
        if idx == 0 or A[idx] > B[idx - 1] and B[idx] > A[idx - 1]:
            A[idx], B[idx] = B[idx], A[idx]
            self.dfs(A, B, idx + 1, current_step + 1)
            A[idx], B[idx] = B[idx], A[idx]

    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        self.dfs(A, B, 0, 0)

        return self.min_step
