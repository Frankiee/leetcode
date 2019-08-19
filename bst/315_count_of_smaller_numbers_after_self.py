# [Important]
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# 315. Count of Smaller Numbers After Self

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


class BstNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.smaller_counts = 0
        self.left = None
        self.right = None


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        ret = []
        root = BstNode(nums.pop())
        ret.insert(0, 0)

        while nums:
            nxt = nums.pop()

            node = root
            count = 0
            while True:
                if node.val == nxt:
                    node.count += 1
                    count += node.smaller_counts
                    break
                elif node.val > nxt:
                    node.smaller_counts += 1
                    if not node.left:
                        node.left = BstNode(nxt)
                        break
                    else:
                        node = node.left
                else:
                    count += (node.smaller_counts + node.count)
                    if not node.right:
                        node.right = BstNode(nxt)
                        break
                    else:
                        node = node.right

            ret.insert(0, count)

        return ret
