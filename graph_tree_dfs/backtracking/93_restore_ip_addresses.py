# [Backtracking]
# https://leetcode.com/problems/restore-ip-addresses/
# 93. Restore IP Addresses

# History:
# Facebook
# 1.
# Mar 10, 2020
# 2.
# May 12, 2020

# Given a string containing only digits, restore it by returning all possible valid IP address
# combinations.
#
# A valid IP address consists of exactly four integers (each integer is between 0 and 255)
# separated by single points.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]


class Solution(object):
    def _dfs(self, s, i, curr, ret):
        if len(curr) > 4:
            return
        if i == len(s):
            if len(curr) == 4:
                ret.append(".".join(curr))
            return

        for nxt_i in range(i + 1, min(len(s) + 1, i + 4)):
            num = s[i:nxt_i]
            if len(num) == 1 or num[0] != '0' and 0 <= int(num) <= 255:
                self._dfs(s, nxt_i, curr + [num], ret)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []

        self._dfs(s, 0, [], ret)

        return ret
