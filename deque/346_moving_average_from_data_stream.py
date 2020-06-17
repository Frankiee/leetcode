# https://leetcode.com/problems/moving-average-from-data-stream/
# 346. Moving Average from Data Stream

# History:
# Facebook
# 1.
# Mar 6, 2020
# 2.
# Apr 30, 2020

# Given a stream of integers and a window size, calculate the moving average of all integers in
# the sliding window.
#
# Example:
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3


from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.buff = deque()
        self.total = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += val
        self.buff.append(val)

        if len(self.buff) > self.size:
            self.total -= self.buff.popleft()

        return self.total / float(len(self.buff))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
