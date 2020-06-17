# https://leetcode.com/problems/sentence-screen-fitting/
# 418. Sentence Screen Fitting

# History:
# Robinhood
# 1.
# Feb 8, 2020

# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how
# many times the given sentence can be fitted on the screen.
#
# Note:
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:
#
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
#
# Output:
# 1
#
# Explanation:
# hello---
# world---
#
# The character '-' signifies an empty space on the screen.
# Example 2:
#
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
#
# Output:
# 2
#
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
#
# The character '-' signifies an empty space on the screen.
# Example 3:
#
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
#
# Output:
# 1
#
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# The character '-' signifies an empty space on the screen.


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if any([len(w) > cols for w in sentence]):
            return 0

        mem = {}

        ret = 0
        curr_word_idx = 0

        curr_col_occupation_count = 0
        for r in range(rows):
            if curr_word_idx in mem:
                ret_diff, nxt_curr_word_idx = mem[curr_word_idx]

                ret += ret_diff
                curr_word_idx = nxt_curr_word_idx
            else:
                nxt_ret = ret
                nxt_curr_word_idx = curr_word_idx

                remaining_count = cols - curr_col_occupation_count

                while True:
                    next_word_len = len(sentence[nxt_curr_word_idx])
                    if remaining_count >= next_word_len:
                        nxt_curr_word_idx += 1
                        if nxt_curr_word_idx >= len(sentence):
                            nxt_ret += 1
                            nxt_curr_word_idx = 0
                        remaining_count -= (next_word_len + 1)
                    else:
                        break

                mem[curr_word_idx] = (nxt_ret - ret, nxt_curr_word_idx)
                curr_word_idx = nxt_curr_word_idx
                ret = nxt_ret

        return ret
