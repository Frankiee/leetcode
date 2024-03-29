# https://leetcode.com/problems/top-k-frequent-words/
# 692. Top K Frequent Words

# History:
# Facebook
# 1.
# Apr 28, 2019
# 2.
# May 12, 2020

# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
#
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
#
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


from collections import Counter, defaultdict


class SolutionCounter(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)

        reverse_counter = defaultdict(list)

        max_freq = 0
        for w, f in counter.iteritems():
            reverse_counter[f].append(w)
            max_freq = max(max_freq, f)

        ret = []
        for i in range(max_freq, -1, -1):
            ret.extend(sorted(reverse_counter[i]))

            if len(ret) >= k:
                ret = ret[:k]
                return ret

        return ret


from collections import Counter
from heapq import heappush, heappop


class WordFrequency(object):
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __eq__(self, other):
        return self.word == other.word and self.frequency == other.frequency

    def __lt__(self, other):
        if self.frequency == other.frequency:
            return self.word > other.word

        return self.frequency < other.frequency


class SolutionMinHeap(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)

        h = []
        for w, c in counter.iteritems():
            heappush(h, WordFrequency(w, c))
            if len(h) > k:
                heappop(h)

        return reversed([heappop(h).word for i in range(len(h))])
