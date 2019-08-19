# [Important]
# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it is able to trap after
# raining.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,
# 1]. In this case, 6 units of rain water (blue section) are being trapped.
# Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


# 1. Two points
class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        leftmax = 0
        rightmax = 0

        res = 0
        while i < j:
            leftmax = max(leftmax, height[i])
            rightmax = max(rightmax, height[j])

            if leftmax < rightmax:
                res += (leftmax - height[i])
                i += 1
            else:
                res += (rightmax - height[j])
                j -= 1

        return res


# 2. Using Stack
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        stack = []
        max_idx = -1

        for i in range(len(height)):
            if not stack:
                if height[i] > 0:
                    stack.append(i)
                    max_idx = i
            else:
                while (stack and height[stack[-1]] <= height[i] and
                       stack[-1] > max_idx):
                    stack.pop()
                stack.append(i)
                if height[i] > 0 and height[i] >= height[max_idx]:
                    max_idx = i

        ret = 0
        for i in range(len(stack)):
            if i > 0:
                min_height = min(height[stack[i]], height[stack[i - 1]])
                ret += min_height * (stack[i] - stack[i - 1] - 1)
                for j in range(stack[i - 1] + 1, stack[i]):
                    ret -= min(min_height, height[j])

        return ret

