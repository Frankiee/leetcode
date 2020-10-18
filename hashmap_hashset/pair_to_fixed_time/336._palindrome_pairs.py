# [Classic, Pair-To-Fixed-Time, Palindrome]
# https://leetcode.com/problems/palindrome-pairs/
# 336. Palindrome Pairs

# history
# Airbnb
# 1.
# Oct 17, 2020

# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list,
# so that the concatenation of the two words words[i] + words[j] is a palindrome.
#
#
#
# Example 1:
#
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:
#
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#
#
# Constraints:
#
# 1 <= words.length <= 5000
# 0 <= words[i] <= 300
# words[i] consists of lower-case English letters.

class Solution(object):
    def _is_palindrome(self, word):
        return word[::-1] == word

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret = []
        word_idx_mp = {
            w: i
            for i, w in enumerate(words)
        }

        for word, word_i in word_idx_mp.iteritems():
            for j in range(len(word) + 1):
                prefix = word[:j]
                surfix = word[j:]

                surfix_reversed = surfix[::-1]
                if (self._is_palindrome(prefix) and surfix_reversed in word_idx_mp and
                        word_idx_mp[surfix_reversed] != word_i):
                    ret.append([word_idx_mp[surfix_reversed], word_i])

                prefix_reversed = prefix[::-1]
                if (self._is_palindrome(surfix) and prefix_reversed in word_idx_mp and
                        word_i != word_idx_mp[prefix_reversed] and j != len(word)):
                    ret.append([word_i, word_idx_mp[prefix_reversed]])

        return ret
