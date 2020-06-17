# https://leetcode.com/problems/add-two-numbers-ii/
# 445. Add Two Numbers II

# History:
# Facebook
# 1.
# Mar 5, 2020
# 2.
# Apr 28, 2020

# You are given two non-empty linked lists representing two non-negative integers. The most
# significant digit comes first and each of their nodes contain a single digit. Add the two
# numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def add_two_numbers(self, l1, l1_length, l2, l2_length):
        if l1_length == l1_length == 0:
            return 0, None

        if l1_length > l2_length:
            carry, rest_ret = self.add_two_numbers(l1.next, l1_length - 1, l2, l2_length)
            curr_sum = carry + l1.val
        elif l1_length < l2_length:
            carry, rest_ret = self.add_two_numbers(l1, l1_length, l2.next, l2_length - 1)
            curr_sum = carry + l2.val
        else:
            carry, rest_ret = self.add_two_numbers(l1.next, l1_length - 1, l2.next, l2_length - 1)
            curr_sum = carry + l2.val + l1.val

        node = ListNode(curr_sum % 10, rest_ret)

        return curr_sum / 10, node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_length = l2_length = 0
        curr_l1, curr_l2 = l1, l2

        while curr_l1:
            l1_length += 1
            curr_l1 = curr_l1.next

        while curr_l2:
            l2_length += 1
            curr_l2 = curr_l2.next

        carry, ret = self.add_two_numbers(l1, l1_length, l2, l2_length)

        if carry > 0:
            return ListNode(carry, ret)

        return ret
