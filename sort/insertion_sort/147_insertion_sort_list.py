# [Insertion-Sort]
# https://leetcode.com/problems/insertion-sort-list/
# 147. Insertion Sort List

# Sort a linked list using insertion sort.
#
#
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
#
#
# Algorithm of Insertion Sort:
#
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Insertion Sort
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        helper = ListNode(float('-inf'))

        loop = helper
        curr = head

        while curr != None:
            nxt = curr.next

            while loop.next != None and loop.next.val < curr.val:
                loop = loop.next

            curr.next = loop.next
            loop.next = curr

            loop = helper
            curr = nxt

        return helper.next
