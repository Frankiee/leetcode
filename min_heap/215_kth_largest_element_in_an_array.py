# https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array

# History:
# 1.
# Apr 1, 2019
# 2.
# Nov 21, 2019

# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


# Min Heap
# Also refer to the Quick Select Solution
# https://www.youtube.com/watch?v=zyskis1Gw0c
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hp = []

        for n in nums:
            heapq.heappush(hp, n)
            if len(hp) > k:
                heapq.heappop(hp)

        return heapq.heappop(hp)
