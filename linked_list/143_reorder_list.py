# https://leetcode.com/problems/reorder-list/
# 143. Reorder List

# History:
# Facebook
# 1.
# Feb 22, 2020

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def _breakup_list(self, head):
        fast, slow = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        reverse_first = slow.next
        slow.next = None

        return reverse_first

    def _reverse_list(self, head):
        # reverse
        reverse_end = head
        head, reverse_second = ListNode(None), head

        while reverse_second:
            temp = head
            head, reverse_second = reverse_second, reverse_second.next
            head.next = temp

        if reverse_end:
            reverse_end.next = None

        return head

    def _merge_list(self, first, second):
        ret = ListNode(None)

        curr = ret
        while first:
            curr.next = first
            first = first.next
            curr.next.next = second
            if second:
                second = second.next
                curr = curr.next.next

        return ret.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        reverse_first = self._breakup_list(head)

        if not reverse_first:
            return head

        reverse_first = self._reverse_list(reverse_first)

        return self._merge_list(head, reverse_first)
