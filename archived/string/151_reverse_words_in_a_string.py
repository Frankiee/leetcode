# [Archived]
# https://leetcode.com/problems/reverse-words-in-a-string/
# 151. Reverse Words in a String

# History:
# Facebook
# 1.
# Dec 9, 2019
# 2.
# May 3, 2020

# Given an input string, reverse the string word by word.
#
# Example 1:
#
# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the
# reversed string.
#
#
# Note:
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not
# contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
# Follow up:
#
# For C programmers, try to solve it in-place in O(1) extra space.


class Solution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = " " + s + " "
        ret = []

        end = None
        for i in range(len(s) - 2, 0, -1):
            if s[i] != ' ' and s[i + 1] == ' ':
                end = i + 1
            if s[i] != ' ' and s[i - 1] == ' ':
                ret.append(s[i:end])

        return " ".join(ret)


class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()

        return ' '.join(reversed(words))
