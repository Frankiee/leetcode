# https://leetcode.com/problems/brace-expansion/
# 1087. Brace Expansion

# History:
# Google
# 1.
# Mar 12, 2020

# A string S represents a list of words.
#
# Each letter in the word has 1 or more options.  If there is one option, the letter is
# represented as is.  If there is more than one option, then curly braces delimit the options.
# For example, "{a,b,c}" represents options ["a", "b", "c"].
#
# For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
#
# Return all words that can be formed in this manner, in lexicographical order.
#
#
#
# Example 1:
#
# Input: "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
# Example 2:
#
# Input: "abcd"
# Output: ["abcd"]
#
#
# Note:
#
# 1 <= S.length <= 50
# There are no nested curly brackets.
# All characters inside a pair of consecutive opening and ending curly brackets are different.


class Solution(object):
    def _dfs(self, S, curr_idx, curr_str, ret):
        if curr_idx == len(S):
            ret.append(curr_str)
            return

        if S[curr_idx] != '{':
            self._dfs(S, curr_idx + 1, curr_str + S[curr_idx], ret)
        else:
            brace_end = curr_idx + 1
            while S[brace_end] != '}':
                brace_end += 1

            strings = S[curr_idx + 1:brace_end]
            options = sorted(strings.split(','))

            for o in options:
                self._dfs(S, brace_end + 1, curr_str + o, ret)

    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret = []
        self._dfs(S, 0, "", ret)
        return ret
