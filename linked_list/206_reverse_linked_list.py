# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List

# History:
# Facebook
# 1.
# Feb 15, 2020
# 2.
# Apr 28, 2020

# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        first = head
        second = head.next
        first.next = None

        while second:
            third = second.next
            second.next = first

            first, second = second, third

        return first
