# [Archived]
# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists

# History:
# Facebook
# 1.
# Mar 12, 2020
# 2.
# Apr 9, 2020
# 3.
# Apr 22, 2020

# Merge two sorted linked lists and return it as a new list. The new list should be made by
# splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = curr = ListNode(None)

        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
            elif l1:
                curr.next = l1
                return ret.next
            else:
                curr.next = l2
                return ret.next

            curr = curr.next

        return ret.next
