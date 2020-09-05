# [Segment-Tree, Classic]
# https://leetcode.com/problems/range-sum-query-mutable/
# 307. Range Sum Query - Mutable

# History:
# Google
# 1.
# Apr 27, 2019
# 2.
# Jun 22, 2020

# Given an integer array nums, find the sum of the elements between indices
# i and j (i <= j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index
# i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.


class SegmentTreeNode(object):
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class NumArray(object):
    def _construct_segment_tree(self, nums, l, r):
        if not nums or l > r:
            return None

        if l == r:
            return SegmentTreeNode(nums[l], l, r)
        else:
            mid = (l + r) / 2
            left_node = self._construct_segment_tree(nums, l, mid)
            right_node = self._construct_segment_tree(nums, mid + 1, r)

            return SegmentTreeNode(
                (left_node.val if left_node else 0) + (right_node.val if right_node else 0),
                l, r, left_node, right_node
            )

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.segment_tree = self._construct_segment_tree(nums, 0, len(nums) - 1)

    def _update_node(self, i, val, curr_node):
        if not curr_node:
            return 0

        if curr_node.start == curr_node.end:
            if curr_node.start == i:
                curr_node.val = val
                return val
            else:
                return 0

        if curr_node.left and curr_node.left.start <= i <= curr_node.left.end:
            left_val = self._update_node(i, val, curr_node.left)

            curr_node.val = left_val + (curr_node.right.val if curr_node.right else 0)
            return curr_node.val

        if curr_node.right and curr_node.right.start <= i <= curr_node.right.end:
            right_val = self._update_node(i, val, curr_node.right)

            curr_node.val = right_val + (curr_node.left.val if curr_node.left else 0)
            return curr_node.val

        return 0

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._update_node(i, val, self.segment_tree)

    def _sum_range_node(self, i, j, curr_node):
        if not curr_node or i > curr_node.end or j < curr_node.start:
            return 0

        if i <= curr_node.start and j >= curr_node.end:
            return curr_node.val

        return (self._sum_range_node(i, j, curr_node.left) +
                self._sum_range_node(i, j, curr_node.right))

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum_range_node(i, j, self.segment_tree)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
