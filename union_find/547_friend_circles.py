# [Union-Find]
# https://leetcode.com/problems/friend-circles/
# 547. Friend Circles

# History:
# 1.
# Apr 28, 2019
# 2.
# Nov 13, 2019
# 3.
# May 4, 2020

# There are N students in a class. Some of them are friends, while some are
# not. Their friendship is transitive in nature. For example, if A is a
# direct friend of B, and B is a direct friend of C, then A is an indirect
# friend of C. And we defined a friend circle is a group of students who are
# direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students
# in the class. If M[i][j] = 1, then the ith and jth students are direct
# friends with each other, otherwise not. And you have to output the total
# number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a
# friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
# students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the
# same friend circle, so return 1.
#
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.


class UnionFindSet(object):
    def __init__(self, n):
        self.parents = range(n)

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        self.parents[i_root] = j_root

    def find_root(self, i):
        # Not root
        if i != self.parents[i]:
            self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]


class SolutionWithoutRank(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0

        union_find_set = UnionFindSet(len(M))

        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union_find_set.union(i, j)

        circles = set()
        for i in range(len(M)):
            circles.add(union_find_set.find_root(i))

        return len(circles)


from collections import defaultdict


class UnionFindWithRank(object):
    def __init__(self):
        self.parents = {}
        self.ranks = defaultdict(int)

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if i_root == j_root:
            return

        if self.ranks[i_root] > self.ranks[j_root]:
            self.parents[j_root] = i_root
        elif self.ranks[i_root] < self.ranks[j_root]:
            self.parents[i_root] = j_root
        else:
            self.parents[i_root] = j_root
            self.ranks[j_root] += 1

    def find_root(self, i):
        if i not in self.parents:
            self.parents[i] = i
        else:
            if self.parents[i] != i:
                self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]


class SolutionWithRank(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        union_find = UnionFindWithRank()

        circles = set()
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    union_find.union(i, j)

        for i in range(len(M)):
            circles.add(union_find.find_root(i))

        return len(circles)
