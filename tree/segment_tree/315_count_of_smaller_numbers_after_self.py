# [Segment-Tree, Classic]
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 315. Count of Smaller Numbers After Self

# History:
# Google
# 1.
# Apr 22, 2019
# 2.
# Jun 15, 2020
# 3.
# Aug 1, 2020

# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.


from collections import deque


class BstNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.smaller_count = 0


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        root = BstNode(nums.pop())
        ret = deque()
        ret.appendleft(0)

        while nums:
            nxt = nums.pop()

            curr_node = root
            count = 0

            while True:
                if curr_node.val == nxt:
                    curr_node.count += 1
                    count += curr_node.smaller_count
                    break
                elif curr_node.val > nxt:
                    curr_node.smaller_count += 1
                    if curr_node.left:
                        curr_node = curr_node.left
                    else:
                        curr_node.left = BstNode(nxt)
                        break
                else:
                    count += (curr_node.count + curr_node.smaller_count)
                    if curr_node.right:
                        curr_node = curr_node.right
                    else:
                        curr_node.right = BstNode(nxt)
                        break

            ret.appendleft(count)

        return ret
