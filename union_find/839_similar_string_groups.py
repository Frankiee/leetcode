# [Union-Find]
# https://leetcode.com/problems/similar-string-groups/
# 839. Similar String Groups

# History:
# Facebook
# 1.
# May 3, 2020

# Two strings X and Y are similar if we can swap two letters (in different positions) of X,
# so that it equals Y. Also two strings X and Y are similar if they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and
# "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group even though they are not similar.
# Formally, each group is such that a word is in the group if and only if it is similar to at
# least one other word in the group.
#
# We are given a list A of strings.  Every string in A is an anagram of every other string in A.
# How many groups are there?
#
#
#
# Example 1:
#
# Input: A = ["tars","rats","arts","star"]
# Output: 2
#
#
# Constraints:
#
# 1 <= A.length <= 2000
# 1 <= A[i].length <= 1000
# A.length * A[i].length <= 20000
# All words in A consist of lowercase letters only.
# All words in A have the same length and are anagrams of each other.


from collections import defaultdict


class UnionFind(object):
    def __init__(self):
        self.parents = {}
        self.rank = defaultdict(int)

    def find_root(self, i):
        if i not in self.parents:
            self.parents[i] = i
        else:
            if self.parents[i] != i:
                self.parents[i] = self.find_root(self.parents[i])

        return self.parents[i]

    def union(self, i, j):
        i_root = self.find_root(i)
        j_root = self.find_root(j)

        if i_root == j_root:
            return

        if self.rank[i_root] > self.rank[j_root]:
            self.parents[j_root] = i_root
        elif self.rank[i_root] < self.rank[j_root]:
            self.parents[i_root] = j_root
        else:
            self.parents[i_root] = j_root
            self.rank[j_root] += 1


class Solution(object):
    def _is_similar(self, str1, str2):
        if len(str1) != len(str2):
            return False

        i1 = i2 = None

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if i1 is None:
                    i1 = i
                elif i2 is None:
                    i2 = i
                else:
                    return False

        if i1 is None:
            return True

        if i1 is not None and i2 is None:
            return False

        return str1[i1], str1[i2] == str2[i2], str2[i1]

    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        A = list(set(A))
        union_find = UnionFind()

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if self._is_similar(A[i], A[j]):
                    union_find.union(A[i], A[j])

        root = set()

        for i in range(len(A)):
            root.add(union_find.find_root(A[i]))

        return len(root)
