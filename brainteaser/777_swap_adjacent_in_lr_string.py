# https://leetcode.com/problems/swap-adjacent-in-lr-string/
# 777. Swap Adjacent in LR String

# History:
# Google
# 1.
# Mar 10, 2020

# Solution:
# https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/217070/Python-using-corresponding-position-

# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of
# either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with
# "XR". Given the starting string start and the ending string end, return True if and only if
# there exists a sequence of moves to transform one string to the other.
#
# Example:
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Note:
#
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        start_nxt_l_r = end_nxt_l_r = 0

        while True:
            while start_nxt_l_r < len(start) and start[start_nxt_l_r] == 'X':
                start_nxt_l_r += 1
            while end_nxt_l_r < len(end) and end[end_nxt_l_r] == 'X':
                end_nxt_l_r += 1

            if start_nxt_l_r == len(start) or end_nxt_l_r == len(end):
                return start_nxt_l_r == end_nxt_l_r == len(start)

            if start[start_nxt_l_r] != end[end_nxt_l_r]:
                return False

            if start[start_nxt_l_r] == 'L':
                if start_nxt_l_r < end_nxt_l_r:
                    return False
            else:
                if start_nxt_l_r > end_nxt_l_r:
                    return False

            start_nxt_l_r += 1
            end_nxt_l_r += 1
