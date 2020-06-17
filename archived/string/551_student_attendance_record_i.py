# [Archived]
# https://leetcode.com/problems/student-attendance-record-i/
# 551. Student Attendance Record I

# History:
# Google
# 1.
# Mar 25, 2020

# You are given a string representing an attendance record for a student. The record only
# contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
# or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent_count = 0

        for idx, c in enumerate(s):
            if c == 'A':
                absent_count += 1

                if absent_count > 1:
                    return False
            elif idx >= 2 and c == 'L' == s[idx - 1] == s[idx - 2]:
                return False

        return True
