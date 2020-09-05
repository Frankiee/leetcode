# [Classic]
# https://leetcode.com/problems/guess-the-word/
# 843. Guess the Word

# History:
# Google
# 1.
# Jun 24, 2020

# This problem is an interactive problem new to the LeetCode platform.
#
# We are given a word list of unique words, each word is 6 letters long, and one word in this
# list is chosen as secret.
#
# You may call master.guess(word) to guess a word.  The guessed word should have type string and
# must be from the original list with 6 lowercase letters.
#
# This function returns an integer type, representing the number of exact matches (value and
# position) of your guess to the secret word.  Also, if your guess is not in the given wordlist,
# it will return -1 instead.
#
# For each test case, you have 10 guesses to guess the word. At the end of any number of calls,
# if you have made 10 or less calls to master.guess and at least one of these guesses was the
# secret, you pass the testcase.
#
# Besides the example test case below, there will be 5 additional test cases, each with 100 words
# in the word list.  The letters of each word in those testcases were chosen independently at
# random from 'a' to 'z', such that every word in the given word lists is unique.
#
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
#
# Explanation:
#
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
#
# We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
# Note:  Any solutions that attempt to circumvent the judge will result in disqualification.


from collections import Counter


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class SolutionMiniMax(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0

        while n < 6:
            counts = [Counter([w[i] for w in wordlist]) for i in range(6)]
            word_guess = max(wordlist, key=lambda w: sum([counts[i][c] for i, c in enumerate(w)]))
            n = master.guess(word_guess)
            wordlist = [w for w in wordlist if sum(c1 == c2 for c1, c2 in zip(w, word_guess)) == n]


class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        for i in range(10):
            guess = random.choice(wordlist)
            guess_result = master.guess(guess)

            wordlist = [
                w
                for w in wordlist
                if guess_result == sum(1 for j in range(6) if w[j] == guess[j])
            ]
