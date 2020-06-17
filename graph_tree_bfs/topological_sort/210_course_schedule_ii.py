# [Classic, Topological-Sort]
# https://leetcode.com/problems/course-schedule-ii/
# 210. Course Schedule II

# History:
# Facebook
# 1.
# Feb 02, 2020
# 2.
# Mar 8, 2020
# 3.
# May 4, 2020

# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course
# 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of
# courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible
# to finish all courses, return an empty array.
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished
# both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read
# more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        in_degree = {}
        out_graph = wfo(list)

        for i in range(numCourses):
            in_degree[i] = 0

        for course, pre in prerequisites:
            in_degree[course] += 1
            out_graph[pre].append(course)

        zero_in_courses = [c for c, f in in_degree.iteritems() if f == 0]

        ret = []
        while in_degree:
            nxt_zero_in_courses = []

            if not zero_in_courses:
                return []

            ret.extend(zero_in_courses)

            for course in zero_in_courses:
                del in_degree[course]

                for out_c in out_graph[course]:
                    if out_c in in_degree:
                        in_degree[out_c] -= 1
                        if in_degree[out_c] == 0:
                            nxt_zero_in_courses.append(out_c)

            zero_in_courses = nxt_zero_in_courses

        return ret
