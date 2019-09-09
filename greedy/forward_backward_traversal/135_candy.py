# [Forward-Backward-Traversal]
# https://leetcode.com/problems/candy/
# 135. Candy

# There are N children standing in a line. Each child is assigned a rating
# value.
#
# You are giving candies to these children subjected to the following
# requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2,
# 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1,
# 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above
#              two conditions.


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        ret = [1] * len(ratings)

        # forward
        for idx in range(len(ratings)):
            if idx > 0 and ratings[idx] > ratings[idx - 1]:
                ret[idx] = ret[idx - 1] + 1

        # backward
        for idx in range(len(ratings) - 1, -1, -1):
            if idx < len(ratings) - 1 and ratings[idx] > ratings[idx + 1]:
                ret[idx] = max(ret[idx], ret[idx + 1] + 1)

        return sum(ret)
