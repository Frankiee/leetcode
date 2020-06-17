# [Union-Find]
# https://leetcode.com/problems/smallest-string-with-swaps/
# 1202. Smallest String With Swaps

# History:
# ByteDance
# 1.
# Sep 29, 2019
# 2.
# Mar 10, 2020

# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
#
# Return the lexicographically smallest string that s can be changed to
# after using the swaps.
#
#
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
#
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
#
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.


from collections import defaultdict


class UnionFindSet(object):
    def __init__(self, n):
        self.parents = range(n)

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parents[i_root] = j_root

    def find_root(self, i):
        # Not root
        if i != self.parents[i]:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        self.union_find_set = UnionFindSet(len(s))

        for p1, p2 in pairs:
            self.union_find_set.union(p1, p2)

        groups = defaultdict(list)

        for i in range(len(s)):
            groups[self.union_find_set.find_root(i)].append(i)

        ret = list(s)
        for group in groups.values():
            sorted_chars = sorted([s[i] for i in group])
            sorted_is = sorted(group)

            for char, i in zip(sorted_chars, sorted_is):
                ret[i] = char

        return ''.join(ret)
