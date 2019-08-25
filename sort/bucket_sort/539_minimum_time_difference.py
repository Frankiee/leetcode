# [BucketSort]
# https://leetcode.com/problems/minimum-time-difference/
# 539. Minimum Time Difference

# Given a list of 24-hour clock time points in "Hour:Minutes" format,
# find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed
# 20000.
# The input time is legal and ranges from 00:00 to 23:59.


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # bucket sort
        time_buckets = [False] * 24 * 60

        for t in timePoints:
            h, m = t.split(":")
            bucket = int(h) * 60 + int(m)
            if time_buckets[bucket]:
                return 0
            time_buckets[bucket] = True

        first = previous = None
        min_diff = float('inf')
        for idx, t in enumerate(time_buckets):
            if t:
                if first is None:
                    first = idx
                if previous is not None:
                    min_diff = min(min_diff, idx - previous)
                previous = idx

        min_diff = min(first + 1440 - previous, min_diff)

        return min_diff
