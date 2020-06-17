# https://leetcode.com/problems/reverse-linked-list-ii/
# 92. Reverse Linked List II

# History:
# Facebook
# 1.
# May 5, 2020

# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = curr = ListNode(None, head)

        for _ in range(m - 1):
            curr = curr.next

        front = curr

        first = curr = curr.next
        nxt = curr.next
        for _ in range(n - m):
            nxt_nxt = nxt.next
            nxt.next = curr

            curr, nxt = nxt, nxt_nxt

        front.next = curr
        first.next = nxt

        return dummy.next
