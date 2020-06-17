# [Merge-Sort]
# https://leetcode.com/problems/sort-list/
# 148. Sort List

# History:
# Facebook
# 1.
# Mar, 20, 2019
# 2.
# Jan, 20, 2019
# 3.
# Apr 24, 2020

# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def _merge_two(self, first, second):
        dummy = curr = ListNode(None)

        while first and second:
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next

            curr = curr.next

        if first:
            curr.next = first
        else:
            curr.next = second

        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None

        first = self.sortList(first)
        second = self.sortList(second)

        return self._merge_two(first, second)
