# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists

# History:
# Facebook
# 1.
# Feb 22, 2020
# 2.
# Apr 12, 2020
# 3.
# Apr 22, 2020

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

from heapq import heappush, heappop


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = curr = ListNode(None)

        pq = []
        for l in lists:
            if l:
                heappush(pq, (l.val, l))

        while pq:
            nxt = heappop(pq)[1]

            curr.next = nxt
            curr = curr.next

            nxt = nxt.next
            if nxt:
                heappush(pq, (nxt.val, nxt))

        return dummy.next
