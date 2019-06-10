# https://leetcode.com/problems/possible-bipartition/
# 886. Possible Bipartition

# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the
# same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two
# groups in this way.
#
#
# Example 1:
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
# Note:
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].


from collections import defaultdict


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if not dislikes:
            return True

        dislikes_map = defaultdict(set)

        for p1, p2 in dislikes:
            dislikes_map[p1].add(p2)
            dislikes_map[p2].add(p1)

        to_visit = [i for i in range(1, N + 1)]
        visited = set()

        group_a = set()
        group_b = set()

        while to_visit:
            next_node = to_visit.pop()
            if next_node in visited:
                continue

            visited.add(next_node)

            if next_node in group_a:
                next_node_group = group_a
                next_node_dislike_group = group_b
            elif next_node in group_b:
                next_node_group = group_b
                next_node_dislike_group = group_a
            else:
                group_a.add(next_node)
                next_node_group = group_a
                next_node_dislike_group = group_b

            next_node_dislikes = dislikes_map[next_node]
            if any([i in next_node_group for i in next_node_dislikes]):
                return False

            for i in next_node_dislikes:
                if i not in next_node_dislike_group:
                    next_node_dislike_group.add(i)
                    to_visit.append(i)

        print group_a, group_b

        return True
