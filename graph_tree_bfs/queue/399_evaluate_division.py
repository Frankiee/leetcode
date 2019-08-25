# [Hard, BFS, Queue]
# https://leetcode.com/problems/evaluate-division/
# 399. Evaluate Division

# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number).
# Given some queries, return the answers. If the answer does not exist,
# return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
#
#
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.


from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        division_tree = defaultdict(dict)

        to_visit = []
        for (dividend, divisor), value in zip(equations, values):
            to_visit.append((dividend, divisor, value))

        while to_visit:
            dividend, divisor, value = to_visit.pop()

            division_tree[dividend][divisor] = value
            division_tree[divisor][dividend] = 1 / value

            for dn, v in division_tree[dividend].iteritems():
                if dn not in division_tree[divisor]:
                    to_visit.append((divisor, dn, 1 / value * v))
            for dn, v in division_tree[divisor].iteritems():
                if dn not in division_tree[dividend]:
                    to_visit.append((dividend, dn, value * v))

        ret = []
        for dividend, divisor in queries:
            if (dividend in division_tree and
                    divisor in division_tree[dividend]):
                ret.append(division_tree[dividend][divisor])
            else:
                ret.append(-1)

        return ret
