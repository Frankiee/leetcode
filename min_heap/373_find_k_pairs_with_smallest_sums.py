# [Classic]
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# 373. Find K Pairs with Smallest Sums

# History:
# Facebook
# 1.
# May 12, 2020

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the
# second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


from heapq import heappush, heappop


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        ret = []
        hp = []

        for nums1_idx, n in enumerate(nums1):
            heappush(hp, (n + nums2[0], nums1_idx, 0))

        while len(ret) < k and hp:
            _, nums1_idx, nums2_idx = heappop(hp)

            ret.append([nums1[nums1_idx], nums2[nums2_idx]])

            if len(ret) == k:
                return ret

            if nums2_idx + 1 < len(nums2):
                heappush(hp, (nums1[nums1_idx] + nums2[nums2_idx + 1], nums1_idx, nums2_idx + 1))

        return ret


from heapq import heappush, heappop


class SolutionWithSet(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        ret = []
        hp = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}

        while len(ret) < k and hp:
            _, n1_idx, n2_idx = heappop(hp)

            ret.append([nums1[n1_idx], nums2[n2_idx]])

            if len(ret) == k:
                return ret

            if n1_idx + 1 < len(nums1) and (n1_idx + 1, n2_idx) not in visited:
                visited.add((n1_idx + 1, n2_idx))
                heappush(hp, (nums1[n1_idx + 1] + nums2[n2_idx], n1_idx + 1, n2_idx))

            if n2_idx + 1 < len(nums2) and (n1_idx, n2_idx + 1) not in visited:
                visited.add((n1_idx, n2_idx + 1))
                heappush(hp, (nums1[n1_idx] + nums2[n2_idx + 1], n1_idx, n2_idx + 1))

        return ret
