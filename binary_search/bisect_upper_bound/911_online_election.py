# [Bisect-Upper-Bound]
# https://leetcode.com/problems/online-election/
# 911. Online Election

# History:
# Google
# 1.
# Jun 22, 2020

# In an election, the i-th vote was cast for persons[i] at time times[i].
#
# Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will
# return the number of the person that was leading the election at time t.
#
# Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote
# (among tied candidates) wins.
#
#
#
# Example 1:
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],
# [3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation:
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
#
# Note:
#
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.vote_winner = []

        curr_max = None
        curr_max_person = None
        votes = [0] * len(persons)
        for p, ts in zip(persons, times):
            votes[p] += 1
            if curr_max is None or votes[p] >= curr_max:
                curr_max = votes[p]
                curr_max_person = p
            self.vote_winner.append((ts, curr_max_person))

    def _bisect_upper(self, t):
        l, r = 0, len(self.vote_winner)

        while l < r:
            m = (r - l) / 2 + l

            if self.vote_winner[m][0] > t:
                r = m
            else:
                l = m + 1

        return l

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        pos = self._bisect_upper(t)

        if pos == 0:
            return None

        return self.vote_winner[pos - 1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
