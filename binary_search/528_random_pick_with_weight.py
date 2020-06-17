# https://leetcode.com/problems/random-pick-with-weight/
# 528. Random Pick with Weight

# History:
# Facebook
# 1.
# Dec 18, 2019
# 2.
# Apr 6, 2020
# 3.
# Apr 12, 2020
# 4.
# May 2, 2020

# Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments. Solution's constructor has
# one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a
# list, even if there aren't any.


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.mem = w
        for i in range(1, len(w)):
            self.mem[i] += self.mem[i - 1]

    def _bisect(self, idx):
        l, r = 0, len(self.mem)

        while l < r:
            m = (r - l) / 2 + l

            if self.mem[m] >= idx:
                r = m
            else:
                l = m + 1

        return l

    def pickIndex(self):
        """
        :rtype: int
        """
        idx = random.randint(1, self.mem[-1])

        return self._bisect(idx)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
