# [Classic, Topological-Sort]
# https://leetcode.com/problems/course-schedule/
# 207. Course Schedule

# History:
# Facebook, Google
# 1.
# Mar 8, 2020
# 2.
# Apr 3, 2020
# 3.
# May 4, 2020

# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course
# 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to
# finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read
# more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


# Time: O(V+E)
# Space:
from collections import defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = {}
        out_graph = defaultdict(list)

        for i in range(numCourses):
            in_degree[i] = 0

        for course, pre in prerequisites:
            in_degree[course] += 1
            out_graph[pre].append(course)

        zero_ins = [c for c, f in in_degree.iteritems() if f == 0]

        while in_degree:
            nxt_zero_ins = []

            if not zero_ins:
                return False

            for c in zero_ins:
                del in_degree[c]
                for out_c in out_graph[c]:
                    if out_c in in_degree:
                        in_degree[out_c] -= 1
                        if in_degree[out_c] == 0:
                            nxt_zero_ins.append(out_c)

            zero_ins = nxt_zero_ins

        return True
