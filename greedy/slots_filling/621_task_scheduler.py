# [Greedy, Slots-Filling]
# https://leetcode.com/problems/task-scheduler/
# 621. Task Scheduler

# History:
# Facebook
# 1.
# Sep 1, 2019
# 2.
# Apr 14, 2020
# 3.
# May 15, 2020

# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks. Tasks
# could be done without original order. Each task could be done in one
# interval. For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing
# different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to
# finish all the given tasks.
#
#
#
# Example:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
#
# Note:
#
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

from collections import Counter


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)

        max_freq = max(counter.values())

        max_freq_task_count = len([c for c, f in counter.iteritems() if f == max_freq])

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_task_count)
