# [Archived, Dummy-Node]
# https://leetcode.com/problems/remove-linked-list-elements/
# 203. Remove Linked List Elements

# History:
# Apple, Google
# 1.
# Mar 21, 2020
# 2.
# Jun 14, 2020

# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SolutionIteration(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr_node = new_head = ListNode(None)
        new_head.next = head

        while curr_node:
            if curr_node.next and curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        return new_head.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionRecrusion(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)

        head.next = self.removeElements(head.next, val)

        return head
