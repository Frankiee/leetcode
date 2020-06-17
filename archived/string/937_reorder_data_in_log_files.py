# [Archived]
# https://leetcode.com/problems/reorder-data-in-log-files/
# 937. Reorder Data in Log Files

# History:
# Google
# 1.
# Jun 13, 2020

# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that
# each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are
# ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The
# digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
#
#
# Example 1:
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#
#
# Constraints:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.


class Solution(object):
    def _get_order_root(self, log):
        log_split = log.split(' ')

        return " ".join(log_split[1:])

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            root = self._get_order_root(log)
            if root[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((root, log))

        letter_logs.sort()

        return [log[1] for log in letter_logs] + digit_logs
