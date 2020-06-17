# https://leetcode.com/problems/strobogrammatic-number-ii/
# 247. Strobogrammatic Number II

# History:
# Facebook
# 1.
# Jan 30, 2020
# 2.
# May 15, 2020

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at
# upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]


class Solution1(object):
    FIRST_NUMS = [
        ('1', '1'),
        ('8', '8'),
        ('6', '9'),
        ('9', '6'),
    ]
    MIDDLE_NUMS = {
        '0',
        '1',
        '8',
    }
    OTHER_NUMS = {
        ('0', '0'),
        ('1', '1'),
        ('8', '8'),
        ('6', '9'),
        ('9', '6'),
    }

    def _dfs(self, i, curr, n, ret):
        if i == n / 2:
            ret.append("".join(curr))
            return

        pairs = self.FIRST_NUMS if i == 0 else self.OTHER_NUMS

        for p1, p2 in pairs:
            nxt = curr[::]
            nxt[i], nxt[n - 1 - i] = p1, p2
            self._dfs(i + 1, nxt, n, ret)

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        if n % 2 == 1:
            for i in self.MIDDLE_NUMS:
                curr = [None] * n
                curr[n / 2] = i
                self._dfs(0, curr, n, ret)
        else:
            curr = [None] * n
            self._dfs(0, curr, n, ret)

        return ret


class Solution2(object):
    ALL_PAIRS = {
        ('6', '9'),
        ('9', '6'),
        ('1', '1'),
        ('8', '8'),
    }
    MIDDLE_NUMBER = ["0", "1", "8"]

    def dfs(self, curr_idx, n, ret, curr_arr):
        if curr_idx > (n - 1) / 2:
            ret.append(''.join(curr_arr))
            return

        if n % 2 == 1 and curr_idx == (n - 1) / 2:
            for f in self.MIDDLE_NUMBER:
                new_arr = copy.deepcopy(curr_arr)
                new_arr[curr_idx] = f
                self.dfs(curr_idx + 1, n, ret, new_arr)
        else:
            for f, s in self.ALL_PAIRS:
                new_arr = copy.deepcopy(curr_arr)
                new_arr[curr_idx] = f
                new_arr[n - 1 - curr_idx] = s
                self.dfs(curr_idx + 1, n, ret, new_arr)

            if curr_idx > 0:
                new_arr = copy.deepcopy(curr_arr)
                new_arr[curr_idx] = '0'
                new_arr[n - 1 - curr_idx] = '0'
                self.dfs(curr_idx + 1, n, ret, new_arr)

    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []

        arr = [None] * n
        self.dfs(0, n, ret, arr)

        return ret
