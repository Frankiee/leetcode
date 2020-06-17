# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# 426. Convert Binary Search Tree to Sorted Doubly Linked List

# History:
# Facebook
# 1.
# Mar 15, 2020
# 2.
# Apr 6, 2020
# 3.
# Apr 24, 2020

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#
# You can think of the left and right pointers as synonymous to the predecessor and successor
# pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the
# first element is the last element, and the successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation, the left pointer of the
# tree node should point to its predecessor, and the right pointer should point to its successor.
# You should return the pointer to the smallest element of the linked list.
#
#
#
# Example 1:
#
#
#
# Input: root = [4,2,5,1,3]
#
#
# Output: [1,2,3,4,5]
#
# Explanation: The figure below shows the transformed BST. The solid line indicates the successor
# relationship, while the dashed line means the predecessor relationship.
#
# Example 2:
#
# Input: root = [2,1,3]
# Output: [1,2,3]
# Example 3:
#
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
# Example 4:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# All values of Node.val are unique.
# 0 <= Number of Nodes <= 2000

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def _tree_to_doubly_list(self, node):
        if not node:
            return None, None

        left_left, left_right = self._tree_to_doubly_list(node.left)
        right_left, right_right = self._tree_to_doubly_list(node.right)

        if left_right:
            left_right.right = node
            node.left = left_right
            left = left_left
        else:
            left = node

        if right_left:
            right_left.left = node
            node.right = right_left
            right = right_right
        else:
            right = node

        return left, right

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        left, right = self._tree_to_doubly_list(root)
        left.left = right
        right.right = left

        return left


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution(object):
    def _tree_to_doubly_list(self, root):
        if not root:
            return None, None

        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root, root

        left_start, left_end = self._tree_to_doubly_list(root.left)
        right_start, right_end = self._tree_to_doubly_list(root.right)

        if left_start:
            left_end.right = root
            root.left = left_end
        else:
            left_start = left_end = root

        if right_start:
            root.right = right_start
            right_start.left = root
        else:
            right_start = right_end = root

        left_start.left = right_end
        right_end.right = left_start

        return left_start, right_end

    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        start, _ = self._tree_to_doubly_list(root)

        return start
