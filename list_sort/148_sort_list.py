# https://leetcode.com/problems/sort-list/
# 148. Sort List

# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                new_head = head.next
                head.next.next = head
                head.next = None
                return new_head
            else:
                return head

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list1 = head
        list2 = slow.next
        slow.next = None

        sorted_list1 = self.sortList(list1)
        sorted_list2 = self.sortList(list2)

        sorted_list = ListNode(None)
        cur = sorted_list

        while sorted_list1 or sorted_list2:
            if not sorted_list1:
                nxt = sorted_list2
                sorted_list2 = sorted_list2.next
            elif not sorted_list2:
                nxt = sorted_list1
                sorted_list1 = sorted_list1.next
            else:
                if sorted_list1.val < sorted_list2.val:
                    nxt = sorted_list1
                    sorted_list1 = sorted_list1.next
                else:
                    nxt = sorted_list2
                    sorted_list2 = sorted_list2.next

            cur.next = nxt
            cur = nxt
            nxt.next = None

        return sorted_list.next
