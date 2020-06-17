# https://leetcode.com/problems/frog-jump/
# 403. Frog Jump

# History:
# Facebook
# 1.
# May 6, 2020

# A frog is crossing a river. The river is divided into x units and at each unit there may or may
# not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog
# is able to cross the river by landing on the last stone. Initially, the frog is on the first
# stone and assume the first jump must be 1 unit.
#
# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1
# units. Note that the frog can only jump in the forward direction.
#
# Note:
#
# The number of stones is ≥ 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.
# Example 1:
#
# [0,1,3,5,6,8,12,17]
#
# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.
#
# Return true. The frog can jump to the last stone by jumping
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then
# 2 units to the 4th stone, then 3 units to the 6th stone,
# 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:
#
# [0,1,2,3,4,8,9,11]
#
# Return false. There is no way to jump to the last stone as
# the gap between the 5th and 6th stone is too large.


from collections import defaultdict


class SolutionDP(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 1:
            return True

        dp = defaultdict(set)
        dp[1].add(1)

        for i in range(1, len(stones)):
            curr_pos = stones[i]
            for step in dp[curr_pos]:
                dp[curr_pos + step].add(step)
                dp[curr_pos + step + 1].add(step + 1)
                if step - 1 > 0:
                    dp[curr_pos + step - 1].add(step - 1)

        return bool(dp[stones[-1]])


class SolutionDP1(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 1:
            return stones[0] == 0

        if stones[0] != 0 or stones[1] != 1:
            return False

        dp = {}

        for s in stones:
            dp[s] = set()

        dp[0].add(0)
        dp[1].add(1)

        for i in range(1, len(stones)):
            pos = stones[i]
            for u in dp[pos]:
                if u > 1:
                    if pos + u - 1 in dp:
                        dp[pos + u - 1].add(u - 1)
                if pos + u in dp:
                    dp[pos + u].add(u)
                if pos + u + 1 in dp:
                    dp[pos + u + 1].add(u + 1)

        return bool(dp[stones[-1]])


class Solution2(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) == 1:
            return stones[0] == 0

        if stones[0] != 0 or stones[1] != 1:
            return False

        dp = [set() for _ in range(len(stones))]
        dp[0] = {0}
        dp[1] = {1}

        pos_idx_mp = dict([(v, i) for i, v in enumerate(stones)])

        for i in range(1, len(stones)):
            pos = stones[i]
            for u in dp[i]:
                if u > 1 and pos + u - 1 in pos_idx_mp:
                    dp[pos_idx_mp[pos + u - 1]].add(u - 1)
                if pos + u in pos_idx_mp:
                    dp[pos_idx_mp[pos + u]].add(u)
                if pos + u + 1 in pos_idx_mp:
                    dp[pos_idx_mp[pos + u + 1]].add(u + 1)

        return bool(dp[-1])
