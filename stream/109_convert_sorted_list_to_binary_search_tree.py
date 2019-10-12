# [Stream]
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# 109. Convert Sorted List to Binary Search Tree

# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ by
# more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the
# following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def from_bst(self, start, end):
        if start > end:
            return None

        mid = (start + end) / 2

        left = self.from_bst(start, mid - 1)

        node = TreeNode(self.head.val)
        self.head = self.head.next

        right = self.from_bst(mid + 1, end)

        node.left = left
        node.right = right

        return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        self.head = head

        end_count = 0
        end = head
        while end.next:
            end_count += 1
            end = end.next

        return self.from_bst(0, end_count)
