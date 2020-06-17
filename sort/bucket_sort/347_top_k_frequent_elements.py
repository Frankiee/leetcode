# [Bucket-Sort, Classic]
# https://leetcode.com/problems/top-k-frequent-elements/
# 347. Top K Frequent Elements

# History:
# Facebook
# 1.
# Apr 28, 2019
# 2.
# Jan 6, 2020
# 3.
# Apr 1, 2020
# 4.
# Apr 22, 2020

# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n
# is the array's size.


from collections import Counter


class SolutionList(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)

        freq_chars = [[] for _ in range(len(nums) + 1)]

        for c, f in counter.iteritems():
            freq_chars[f].append(c)

        ret = []
        for f in range(len(freq_chars) - 1, -1, -1):
            if freq_chars[f]:
                ret.extend(freq_chars[f])

                if len(ret) >= k:
                    return ret


from collections import Counter, defaultdict


class SolutionDict(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)

        freq_chars = defaultdict(list)
        max_freq = 0

        for c, f in counter.iteritems():
            freq_chars[f].append(c)
            max_freq = max(max_freq, f)

        ret = []
        for i in range(max_freq, -1, -1):
            if i in freq_chars:
                ret.extend(freq_chars[i])

            if len(ret) >= k:
                return ret


from heapq import heappush, heappop


class SolutionHeapDeprecated(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)

        hp = []
        for n, c in counter.iteritems():
            heappush(hp, (c, n))

            if len(hp) > k:
                heappop(hp)

        return reversed([heappop(hp)[1] for i in range(len(hp))])
