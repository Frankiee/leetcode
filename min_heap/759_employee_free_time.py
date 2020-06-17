# [Classic]
# https://leetcode.com/problems/employee-free-time/
# 759. Employee Free Time

# History:
# Facebook
# 1.
# Apr 28, 2020
# 2.
# May 6, 2020

# We are given a list schedule of employees, which represents the working time for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free time for all
# employees, also in sorted order.
#
# (Even though we are representing Intervals in the form [x, y], the objects inside are
# Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2,
# and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our
# answer, as they have zero length.
#
#
#
# Example 1:
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
#
#
# Constraints:
#
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8


"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution1(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        schedule = sorted([i for s in schedule for i in s], key=lambda i: i.start)

        ret = []
        pre = schedule[0]

        for i in schedule[1:]:
            if i.start <= pre.end and i.end > pre.end:
                pre.end = i.end
            elif i.start > pre.end:
                ret.append(Interval(pre.end, i.start))
                pre = i

        return ret


from heapq import heappush, heappop

"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""


class Solution2(object):
    START = 1
    END = 2

    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        employee_count = len(schedule)

        free_employee = set(range(employee_count))

        pq = []
        for i, s in enumerate(schedule):
            if s:
                heappush(pq, (s[0].start, s, i, self.START, 0))

        ret = []
        pre_free_start_time = None
        while pq:
            ts, schedule, employee_id, tp, idx = heappop(pq)

            if tp == self.START:
                if (len(free_employee) == employee_count and
                        pre_free_start_time and ts != pre_free_start_time):
                    ret.append(Interval(pre_free_start_time, ts))
                    pre_free_start_time = None
                free_employee.remove(employee_id)
                heappush(pq, (schedule[idx].end, schedule, employee_id, self.END, idx))
            else:
                free_employee.add(employee_id)
                if len(free_employee) == employee_count:
                    pre_free_start_time = ts

                if idx < len(schedule) - 1:
                    heappush(pq,
                             (schedule[idx + 1].start, schedule, employee_id, self.START, idx + 1))

        return ret
