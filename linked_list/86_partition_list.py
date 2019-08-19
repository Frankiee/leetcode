# [Important, DummyNode]
# https://leetcode.com/problems/partition-list/
# 86. Partition List

# Given a linked list and a value x, partition it such that all nodes less
# than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of
# the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_than_dummy = ListNode(None)
        greater_than_equal_dummy = ListNode(None)

        less_than_dummy_p = less_than_dummy
        greater_than_equal_dummy_p = greater_than_equal_dummy

        p = head
        while p:
            next_p = p.next
            if p.val < x:
                less_than_dummy_p.next = p
                less_than_dummy_p = p
                less_than_dummy_p.next = None
            else:
                greater_than_equal_dummy_p.next = p
                greater_than_equal_dummy_p = p
                greater_than_equal_dummy_p.next = None
            p = next_p

        less_than_dummy_p.next = greater_than_equal_dummy.next
        return less_than_dummy.next
