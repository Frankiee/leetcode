# https://leetcode.com/problems/range-sum-query-mutable/
# 307. Range Sum Query - Mutable

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
    def _construct_segment_tree(self, nums, start, end):
        if not nums:
            return None

        if start == end:
            return SegmentTreeNode(nums[start], start, end)
        else:
            mid = (start + end) / 2
            left_node = self._construct_segment_tree(nums, start, mid)
            right_node = self._construct_segment_tree(nums, mid + 1, end)
            return SegmentTreeNode(
                left_node.val + right_node.val,
                start, end, left_node, right_node,
            )

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.segment_tree = self._construct_segment_tree(
            nums, 0, len(nums) - 1)

    def _update_node(self, i, val, current_node):
        if not current_node:
            return 0

        if current_node.start == current_node.end:
            if current_node.start == i:
                current_node.val = val
                return val
            else:
                return 0

        if (current_node.left and
                current_node.left.start <= i <= current_node.left.end):
            new_left_val = self._update_node(i, val, current_node.left)
            current_node.val = new_left_val + (
                current_node.right.val if current_node.right else 0)
            return current_node.val

        if (current_node.right and
                current_node.right.start <= i <= current_node.right.end):
            new_right_val = self._update_node(i, val, current_node.right)
            current_node.val = new_right_val + (
                current_node.left.val if current_node.left else 0)
            return current_node.val

        return 0

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._update_node(i, val, self.segment_tree)

    def _sum_range_node(self, i, j, current_node):
        if not current_node or i > current_node.end or j < current_node.start:
            return 0

        if i <= current_node.start and j >= current_node.end:
            return current_node.val

        return (self._sum_range_node(i, j, current_node.left) +
                self._sum_range_node(i, j, current_node.right))

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
