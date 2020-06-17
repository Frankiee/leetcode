# [Classic, Eulerian-Path]
# https://leetcode.com/problems/reconstruct-itinerary/
# 332. Reconstruct Itinerary

# History:
# Facebook
# 1.
# Mar 7, 2020
# 2.
# Mar 10, 2020
# 3.
# Apr 14, 2020
# 4.
# May 4, 2020

# https://www.youtube.com/watch?v=LKSdX31pXjY

# Given a list of airline tickets represented by pairs of departure and arrival airports [from,
# to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from
# JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest
# lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a
# smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.


from collections import defaultdict, deque


# O(ELogE)
class SolutionEulerianPath(object):
    def _dfs(self, f, out_graph, ret):
        while out_graph[f]:
            self._dfs(out_graph[f].popleft(), out_graph, ret)

        ret.append(f)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets.sort()
        out_graph = defaultdict(deque)

        for f, t in tickets:
            out_graph[f].append(t)

        ret = []
        self._dfs('JFK', out_graph, ret)

        return reversed(ret)


class SolutionDFS(object):
    def _dfs(self, out, tickets, from_city, ret):
        if len(ret) == len(tickets):
            ret.append(from_city)
            return True

        for i in range(len(out[from_city])):
            nxt_city = out[from_city].pop(i)
            ret.append(from_city)
            if self._dfs(out, tickets, nxt_city, ret):
                return True
            out[from_city].insert(i, nxt_city)
            ret.pop(-1)

        return False

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tickets = sorted(tickets)

        out = defaultdict(list)

        for from_city, to_city in tickets:
            out[from_city].append(to_city)

        ret = []
        self._dfs(out, tickets, 'JFK', ret)

        return ret
