# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# 719. Find K-th Smallest Pair Distance

# https://www.youtube.com/watch?v=WHfljqX61Y8&t=1180s

# Given an integer array, return the k-th smallest distance among all the
# pairs. The distance of a pair (A, B) is defined as the absolute difference
# between A and B.
#
# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.


# Heap
import heapq


class Solution1(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        heap = [
            (nums[i + 1] - nums[i], i, i + 1)
            for i in range(len(nums) - 1)
        ]

        heapq.heapify(heap)

        for _ in range(k):
            dist, base, neighbour = heapq.heappop(heap)

            if neighbour + 1 < len(nums):
                heapq.heappush(
                    heap,
                    (
                        nums[neighbour + 1] - nums[base],
                        base,
                        neighbour + 1
                    )
                )

        return dist


# Binary Search
class Solution2(object):
    def _le_m_count(self, m, nums):
        count = 0

        j = 1
        for i in range(len(nums) - 1):
            while j < len(nums) and nums[j] - nums[i] <= m:
                j += 1

            count += j - i - 1

        return count

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        l = 0
        r = nums[-1] - nums[0] + 1

        while l < r:
            m = l + (r - l) / 2

            m_count = self._le_m_count(m, nums)

            if m_count >= k:
                r = m
            else:
                l = m + 1

        return l
