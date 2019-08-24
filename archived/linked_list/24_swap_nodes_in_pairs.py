# [Archived, DummyNode]
# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may
# be changed.
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(None)
        dummy.next = head
        prv = dummy

        while prv.next and prv.next.next:
            p1 = prv.next
            p2 = prv.next.next

            p1.next = p2.next
            prv.next = p2
            p2.next = p1
            prv = p1

        return dummy.next
