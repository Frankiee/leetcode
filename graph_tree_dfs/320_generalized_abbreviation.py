# https://leetcode.com/problems/generalized-abbreviation/
# 320. Generalized Abbreviation

# History:
# Google
# 1.
# Mar 25, 2020
# 2.
# Apr 26, 2020

# Write a function to generate the generalized abbreviations of a word.
#
# Note: The order of the output does not matter.
#
# Example:
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2",
# "2r1", "3d", "w3", "4"]


class SolutionIterating(object):
    def _dfs(self, word, i, curr, ret):
        if i == len(word):
            ret.append(curr)
            return

        if not curr or curr[-1].isdigit():
            for j in range(i + 1, len(word) + 1):
                self._dfs(word, j, curr + word[i:j], ret)

        if not curr or not curr[-1].isdigit():
            for j in range(i + 1, len(word) + 1):
                self._dfs(word, j, curr + str(j - i), ret)

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = []

        self._dfs(word, 0, "", ret)

        return ret


class Solution(object):
    def _dfs(self, word, s_idx, curr, ret):
        if s_idx == len(word):
            ret.append(curr)
            return

        self._dfs(word, s_idx + 1, curr + word[s_idx], ret)

        if not curr or not curr[-1].isdigit():
            for l in range(1, len(word) - s_idx + 1):
                self._dfs(word, s_idx + l, curr + str(l), ret)

    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = []

        self._dfs(word, 0, "", ret)

        return ret
