# [Prefix-Sum]
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
# 1170. Compare Strings by Frequency of the Smallest Character

# History:
# Google
# 1.
# Mar 9, 2020

# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the
# smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest
# character is "c" and its frequency is 2.
#
# Now, given string arrays queries and words, return an integer array answer, where each answer[
# i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
#
#
#
# Example 1:
#
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
# Example 2:
#
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa")
# and f("aaaa") are both > f("cc").
#
#
# Constraints:
#
# 1 <= queries.length <= 2000
# 1 <= words.length <= 2000
# 1 <= queries[i].length, words[i].length <= 10
# queries[i][j], words[i][j] are English lowercase letters.


class Solution(object):
    def _f(self, word):
        min_char = None
        min_char_freq = 0

        for c in word:
            if not min_char or c < min_char:
                min_char = c
                min_char_freq = 1
            elif c == min_char:
                min_char_freq += 1

        return min_char_freq

    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words_min_frequency = [self._f(w) for w in words]

        word_frequency_array = [0] * 12

        for w in words_min_frequency:
            word_frequency_array[w] += 1

        curr_sum = 0
        for i in range(len(word_frequency_array) - 1, -1, -1):
            curr_sum += word_frequency_array[i]
            word_frequency_array[i] = curr_sum

        return [word_frequency_array[self._f(q) + 1] for q in queries]
