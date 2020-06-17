# https://leetcode.com/problems/minimum-genetic-mutation/
# 433. Minimum Genetic Mutation

# History:
# Cruise
# 1.
# May 19, 2020

# A gene string can be represented by an 8-character long string, with choices from "A", "C",
# "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE
# mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be
# in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of
# mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
#
#
# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
#
#
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
#
#
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3


class Solution(object):
    CHARS = ['A', 'C', 'G', 'T']

    def _get_neighbours(self, gene, bank):
        ret = []
        for i in range(len(gene)):
            for c in self.CHARS:
                nxt = gene[:i] + c + gene[i + 1:]
                if nxt in bank:
                    ret.append(nxt)
                    bank.remove(nxt)

        return ret

    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1

        to_check = [start]
        bank = set(bank)
        if start in bank:
            bank.remove(start)

        step = 0
        while to_check:
            next_to_check = []

            for gene in to_check:
                if gene == end:
                    return step

                neis = self._get_neighbours(gene, bank)
                next_to_check.extend(neis)

            if not next_to_check:
                return -1

            step += 1
            to_check = next_to_check

        return step
