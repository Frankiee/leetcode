# [Classic]
# https://leetcode.com/problems/text-justification/
# 68. Text Justification

# History:
# Cruise
# 1.
# May 17, 2020

# Given an array of words and a width maxWidth, format the text such that each line has exactly
# maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each
# line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces
# on a line do not divide evenly between words, the empty slots on the left will be assigned more
# spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between
# words.
#
# Note:
#
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
# Example 1:
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
# Example 3:
#
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        curr, curr_length, ret = [], 0, []

        for word in words:
            if curr_length + len(curr) + len(word) > maxWidth:
                for i in range(maxWidth - curr_length):
                    curr[i % ((len(curr) - 1) or 1)] += ' '
                ret.append("".join(curr))
                curr_length = 0
                curr = []

            curr.append(word)
            curr_length += len(word)

        if curr:
            curr = " ".join(curr)
            curr += " " * (maxWidth - len(curr))
            ret.append(curr)

        return ret
