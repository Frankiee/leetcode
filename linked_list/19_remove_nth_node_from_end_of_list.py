# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 19. Remove Nth Node From End of List

# History:
# Facebook
# 1.
# Mar 29, 2020
# 2.
# May 2, 2020

# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        r = dummy

        for _ in range(n + 1):
            r = r.next

        l = dummy

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next
