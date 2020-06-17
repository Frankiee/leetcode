# [Archived, Dummy-Node]
# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# History:
# Facebook
# 1.
# Apr 30, 2020

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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        first, second, third = head, head.next, head.next.next

        second.next = first
        first.next = self.swapPairs(third)

        return second
