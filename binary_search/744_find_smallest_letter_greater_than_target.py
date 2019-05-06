# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# 744. Find Smallest Letter Greater Than Target

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
        l = 0
        r = len(letters)

        while l < r:
            m = l + (r - l) / 2

            if ord(letters[m]) <= ord(target):
                l = m + 1
            else:
                r = m

        if l < len(letters):
            return letters[l]
        else:
            return letters[0]
