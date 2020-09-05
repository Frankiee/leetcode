# [DP-Sequence-Action, Classic]
# https://leetcode.com/problems/student-attendance-record-ii/
# 552. Student Attendance Record II

# History:
# Google
# 1.
# Jun 24, 2020

# Given a positive integer n, return the number of all possible attendance records with length n,
# which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
#
# A student attendance record is a string that only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more
# than two continuous 'L' (late).
#
# Example 1:
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times.
# Note: The value of n won't exceed 100,000.


class Solution(object):
    MOD = 10 ** 9 + 7

    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        # A L, A L L, A P, no-A L, no-A L L, no-A P
        dp = [0, 0, 1, 1, 0, 1]

        for i in range(1, n):
            dp = [
                dp[2] % self.MOD,
                dp[0] % self.MOD,
                sum(dp) % self.MOD,
                dp[5] % self.MOD,
                dp[3] % self.MOD,
                (dp[3] + dp[4] + dp[5]) % self.MOD,
            ]

        return sum(dp) % self.MOD
