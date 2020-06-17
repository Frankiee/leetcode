# [Greedy, Classic, Stack]
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 1081. Smallest Subsequence of Distinct Characters

# History:
# 1.
# TikTok
# May 22, 2020

# Return the lexicographically smallest subsequence of text that contains all the distinct
# characters of text exactly once.
#
# Example 1:
#
# Input: "cdadabcc"
# Output: "adbc"
# Example 2:
#
# Input: "abcd"
# Output: "abcd"
# Example 3:
#
# Input: "ecbacba"
# Output: "eacb"
# Example 4:
#
# Input: "leetcode"
# Output: "letcod"
#
#
# Constraints:
#
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/


class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        stack = []
        used = set()
        counter = Counter(text)

        for c in text:
            counter[c] -= 1

            if c in used:
                continue

            while stack and ord(stack[-1]) > ord(c) and counter[stack[-1]] > 0:
                used.remove(stack[-1])
                stack.pop(-1)

            stack.append(c)
            used.add(c)

        return "".join(stack)
