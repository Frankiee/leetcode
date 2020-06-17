# [2-Pointers-Sliding-Window, Trap-Water]
# https://leetcode.com/problems/trapping-rain-water/
# 42. Trapping Rain Water

# History:
# 1.
# Mar 31, 2019
# 2.
# Nov 29, 2019
# Daily Interview Pro - Uber
# 3.
# Apr 8, 2020
# 4.
# Apr 22, 2020

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
class SolutionTwoPointers(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_left, max_right = 0, 0

        ret = 0
        while l < r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])

            if max_left < max_right:
                ret += max_left - height[l]
                l += 1
            else:
                ret += max_right - height[r]
                r -= 1

        return ret


# 2. Using Stack
# Extra space needed
class SolutionStack(object):
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


# Extra space needed
class SolutionDP(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        dp = [0] * len(height)

        curr_max = 0
        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            dp[i] = curr_max

        ret = 0
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            curr_max = max(curr_max, height[i])
            dp[i] = min(dp[i], curr_max)
            ret += dp[i] - height[i]

        return ret
