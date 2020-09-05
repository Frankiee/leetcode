# https://leetcode.com/problems/expressive-words/
# 809. Expressive Words

# History:
# Google
# 1.
# Jun 28, 2020

# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo",
# "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that
# are all the same:  "h", "eee", "ll", "ooo".
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by any
# number of applications of the following extension operation: choose a group consisting of
# characters c, and add some number of characters c to the group so that the size of the group is
# 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo",
# but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do
# another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the
# query word "hello" would be stretchy because of these two extension operations: query = "hello"
# -> "hellooo" -> "helllllooo" = S.
#
# Given a list of query words, return the number of words that are stretchy.
#
#
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
#
#
# Notes:
#
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters


class Solution(object):
    def _is_expressive_word(self, s, w):
        w_i = 0

        for s_i in range(len(s)):
            if w_i < len(w) and s[s_i] == w[w_i]:
                w_i += 1
            elif not (s_i + 1 < len(s) and s[s_i] == s[s_i - 1] == s[s_i + 1] or
                      s[s_i] == s[s_i - 1] == s[s_i - 2]):
                return False

        return w_i == len(w)

    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        return sum(
            [self._is_expressive_word(S, w) for w in words]
        )
