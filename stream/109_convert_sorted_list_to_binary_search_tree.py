# [Classic, Stream]
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# 109. Convert Sorted List to Binary Search Tree

# History:
# Facebook
# 1.
# Mar 18, 2020
# 2.
# Apr 1, 202012691269
# 3.
# Apr 13, 2020
# 4.
# May 11, 2020

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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def _sorted_list_to_bst(self, length):
        if length == 0:
            return None

        left_count = length / 2

        left = self._sorted_list_to_bst(left_count)

        root = TreeNode(self.head.val)
        self.head = self.head.next

        right = self._sorted_list_to_bst(length - left_count - 1)

        root.left = left
        root.right = right

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head
        count = 0
        curr = head

        while curr:
            curr = curr.next
            count += 1

        return self._sorted_list_to_bst(count)


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

class Solution2(object):
    def _form_bst(self, l, r):
        if l >= r:
            return None

        m = (l + r) / 2

        left_tree = self._form_bst(l, m)

        node = TreeNode(self.head.val)
        self.head = self.head.next
        right_tree = self._form_bst(m + 1, r)

        node.left = left_tree
        node.right = right_tree

        return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.head = head

        size = 0
        while head:
            size += 1
            head = head.next

        return self._form_bst(0, size)
