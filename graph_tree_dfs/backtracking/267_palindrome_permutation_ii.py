# [Backtracking, Classic]
# https://leetcode.com/problems/palindrome-permutation-ii/
# 267. Palindrome Permutation II

# History:
# Facebook
# 1.
# Mar 17, 2020

# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an
# empty list if no palindromic permutation could be form.
#
# Example 1:
#
# Input: "aabb"
# Output: ["abba", "baab"]
# Example 2:
#
# Input: "abc"
# Output: []


from collections import Counter


class Solution(object):
    def _dfs(self, ret, curr, used, nums):
        if len(curr) == len(nums):
            ret.append(curr)
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            self._dfs(ret, curr + str(nums[i]), used, nums)
            used[i] = False

    def _permute_unique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = [False] * len(nums)

        ret = []
        nums.sort()
        self._dfs(ret, "", used, nums)
        return ret

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_counter = Counter(s)

        odd_char = None
        for c, freq in s_counter.iteritems():
            if freq % 2 == 1:
                if odd_char is not None:
                    return []

                odd_char = c

        if odd_char:
            s_counter[odd_char] -= 1

        chars = []
        for c, freq in s_counter.iteritems():
            chars.extend([c] * (freq / 2))

        middle = odd_char if odd_char else ""

        permus = self._permute_unique(chars)

        ret = []
        for p in permus:
            ret.append(
                p + middle + p[::-1]
            )

        return ret
