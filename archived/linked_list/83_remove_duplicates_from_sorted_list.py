# [Archived]
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List

# History:
# Apple
# 1.
# Mar 21, 2020

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_head = head

        while curr_head:
            if curr_head.next and curr_head.val == curr_head.next.val:
                curr_head.next = curr_head.next.next
            else:
                curr_head = curr_head.next

        return head
