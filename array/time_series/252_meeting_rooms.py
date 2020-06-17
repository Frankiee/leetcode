# [Time-Series]
# https://leetcode.com/problems/meeting-rooms/
# 252. Meeting Rooms

# History:
# 1.
# Feb 21, 2020

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],
# ...] (si < ei), determine if a person could attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition
# to get new method signature.


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals)

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
