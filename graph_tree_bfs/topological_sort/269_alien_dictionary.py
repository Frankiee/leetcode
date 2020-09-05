# [Topological-Sort, Classic]
# https://leetcode.com/problems/alien-dictionary/
# 269. Alien Dictionary

# History:
# Facebook, Google
# 1.
# Feb 02, 2020
# 2.
# Mar 29, 2020
# 3.
# Apr 11, 2020
# 4.
# May 4, 2020
# 5.
# Aug 1, 2020

# There is a new alien language which uses the latin alphabet. However, the order among letters
# are unknown to you. You receive a list of non-empty words from the dictionary, where words are
# sorted lexicographically by the rules of this new language. Derive the order of letters in this
# language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".
# Note:
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.


from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        in_degree = {}
        out_graph = defaultdict(list)

        for word in words:
            for c in word:
                in_degree[c] = 0

        for i in range(1, len(words)):
            for j in range(min(len(words[i - 1]), len(words[i]))):
                if words[i - 1][j] != words[i][j]:
                    in_degree[words[i][j]] += 1
                    out_graph[words[i - 1][j]].append(words[i][j])
                    break

                if j == min(len(words[i - 1]), len(words[i])) - 1 and len(words[i - 1]) > len(
                    words[i]):
                    return ""

        zero_ins = [c for c, f in in_degree.iteritems() if f == 0]

        ret = []
        while in_degree:
            if not zero_ins:
                return ""

            nxt_zero_ins = []

            ret.extend(zero_ins)

            for in_c in zero_ins:
                del in_degree[in_c]
                for out_c in out_graph[in_c]:
                    if out_c in in_degree:
                        in_degree[out_c] -= 1
                        if in_degree[out_c] == 0:
                            nxt_zero_ins.append(out_c)

            zero_ins = nxt_zero_ins

        return "".join(ret)
