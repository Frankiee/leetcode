# https://leetcode.com/problems/longest-well-performing-interval/
# 1124. Longest Well-Performing Interval

# We are given hours, a list of the number of hours worked per day for a
# given employee.
#
# A day is considered to be a tiring day if and only if the number of hours
# worked is (strictly) greater than 8.
#
# A well-performing interval is an interval of days for which the number of
# tiring days is strictly larger than the number of non-tiring days.
#
# Return the length of the longest well-performing interval.
#
#
#
# Example 1:
#
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
#
#
# Constraints:
#
# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        for i in range(len(hours)):
            hours[i] = 1 if hours[i] > 8 else -1

        if sum(hours) > 0:
            return len(hours)

        first_appear = {0: -1}
        longest = 0
        running_score = 0
        for i in range(len(hours)):
            running_score += hours[i]
            if running_score not in first_appear:
                first_appear[running_score] = i
            if running_score - 1 in first_appear:
                longest = max(longest, i - first_appear[running_score - 1])

        return longest
