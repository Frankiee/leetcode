# [Important]
# https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        slow = head
        fast = head
        stack = [head.val]

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)

        if not fast.next:
            stack.pop()

        slow = slow.next
        while slow:
            if not stack or slow.val != stack.pop():
                return False
            slow = slow.next

        return True
