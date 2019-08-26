# [Merge-Sort]
# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
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


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                next_node = l1
                l1 = l1.next
            else:
                next_node = l2
                l2 = l2.next
            tail.next = next_node
            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next

    def _merge(self, lists, l, r):
        if l > r:
            return []
        if l == r:
            return lists[l]
        if l + 1 == r:
            return self._merge_two_lists(lists[l], lists[r])

        m = (l + r) / 2
        left_half_list = self._merge(lists, l, m - 1)
        right_half_list = self._merge(lists, m, r)
        return self._merge_two_lists(left_half_list, right_half_list)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self._merge(lists, 0, len(lists) - 1)
