# [Classic, Time-Series]
# https://leetcode.com/problems/meeting-rooms-ii/
# 253. Meeting Rooms II

# History:
# Facebook
# 1.
# Feb 22, 2020
# 2.
# Apr 2, 2020
# 3.
# Apr 24, 2020
# 4.
# May 5, 2020

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],
# ...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition
# to get new method signature.


class SolutionTimeSeries(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))

        events.sort()

        curr = 0
        ret = 0
        for _, delta in events:
            curr += delta
            ret = max(ret, curr)

        return ret


from heapq import heappop, heappush


class SolutionHeap(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()

        ending_time_hp = []
        ret = 0

        for s, e in intervals:
            while ending_time_hp and ending_time_hp[0] <= s:
                heappop(ending_time_hp)

            heappush(ending_time_hp, e)

            ret = max(ret, len(ending_time_hp))

        return ret
