# https://leetcode.com/problems/reverse-nodes-in-k-group/
# 25. Reverse Nodes in k-Group

# History:
# 1.
# Feb 3, 2020
# 2.
# Apr 26, 2020
# 3.
# May 20, 2020

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the
# number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 1:
            return head

        curr = head
        for i in range(k - 1):
            curr = curr.next
            if not curr:
                return head

        first, second = head, head.next
        for i in range(k - 1):
            third = second.next
            second.next = first
            first, second = second, third

        head.next = self.reverseKGroup(second, k)

        return first
