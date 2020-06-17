# https://leetcode.com/problems/palindrome-permutation/
# 266. Palindrome Permutation

# History:
# Facebook
# 1.
# Jan 4, 2020
# 2.
# May 4, 2020

# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true


from collections import defaultdict


class SolutionOnePass(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = defaultdict(int)
        old_count = 0

        for c in s:
            counter[c] += 1
            if counter[c] % 2 == 0:
                old_count -= 1
            else:
                old_count += 1

        return old_count <= 1


from collections import Counter


class SolutionDeprecated(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str sd
        :rtype: bool
        """
        counter = Counter(s)

        odd_count = 0
        for char, count in counter.iteritems():
            if count % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False

        return True
