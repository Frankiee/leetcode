# https://leetcode.com/problems/number-of-days-between-two-dates/
# 1360. Number of Days Between Two Dates

# History:
# Apple
# 1.
# Mar 29, 2020
# 2.
# Apr 9, 2020

# Write a program to count the number of days between two dates.
#
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
#
#
#
# Example 1:
#
# Input: date1 = "2019-06-29", date2 = "2019-06-30"
# Output: 1
# Example 2:
#
# Input: date1 = "2020-01-15", date2 = "2019-12-31"
# Output: 15
#
#
# Constraints:
#
# The given dates are valid dates between the years 1971 and 2100.


class Solution(object):
    MONTH_DATES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def _days_since_epoch(self, date):
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        date_diff = 365 * (year - 1970)
        for y in range(1970, year):
            if y % 4 == 0:
                date_diff += 1

        for m in range(1, month):
            date_diff += self.MONTH_DATES[m - 1]

        if year % 4 == 0 and year != 2100 and month > 2:
            date_diff += 1

        date_diff += day

        return date_diff

    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        return abs(
            self._days_since_epoch(date1) -
            self._days_since_epoch(date2)
        )
