# [Archived, Dummy-Node]
# https://leetcode.com/problems/odd-even-linked-list/
# 328. Odd Even Linked List

# History:
# Facebook
# 1.
# Apr 13, 2020
# 2.
# May 5, 2020

# Given a singly linked list, group all odd nodes together followed by the
# even nodes. Please note here we are talking about the node number and not
# the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# Note:
#
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_dummy = curr_odd = ListNode(None)
        even_dummy = curr_even = ListNode(None)

        is_odd = True
        curr = head
        while curr:
            if is_odd:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            else:
                curr_even.next = curr
                curr_even = curr_even.next
            curr = curr.next
            is_odd = False if is_odd else True

        curr_even.next = None
        curr_odd.next = even_dummy.next

        return odd_dummy.next
