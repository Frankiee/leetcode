# https://leetcode.com/problems/binary-search-tree-iterator/
# 173. Binary Search Tree Iterator

# Implement an iterator over a binary search tree (BST). Your iterator will
# be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Example:
#
#
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#
#
# Note:
#
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will
# be at least a next smallest number in the BST when next() is called.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._push_all_left(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        next_node = self.stack.pop()
        self._push_all_left(next_node.right)
        return next_node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack

    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
