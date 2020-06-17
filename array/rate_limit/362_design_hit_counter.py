# [Classic, Rate-Limit]
# https://leetcode.com/problems/design-hit-counter/
# 362. Design Hit Counter

# History:
# Google, Netflix
# 1.
# Mar 11, 2020
# 2.
# Jun 7, 2020

# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that
# calls are being made to the system in chronological order (ie, the timestamp is monotonically
# increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?


from collections import deque


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])

        self.count += 1

        while self.queue and self.queue[0][0] <= timestamp - 300:
            _, second_count = self.queue.popleft()
            self.count -= second_count

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.queue and self.queue[0][0] <= timestamp - 300:
            _, second_count = self.queue.popleft()
            self.count -= second_count

        return self.count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
