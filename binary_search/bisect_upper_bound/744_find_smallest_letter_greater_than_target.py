# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 744. Find Smallest Letter Greater Than Target

# History:
# Linkedin
# 1.
# May 5, 2019
# 2.
# Feb 20, 2020
# 3.
# Apr 11, 2021

# Given a list of sorted characters letters containing only lowercase
# letters, and given a target letter target, find the smallest element in
# the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique
# letters.
# target is a lowercase letter.


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l, r = 0, len(letters)

        while l < r:
            m = (r - l) / 2 + l

            if letters[m] > target:
                r = m
            else:
                l = m + 1

        return letters[l] if l < len(letters) else letters[0]
