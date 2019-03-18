# https://leetcode.com/problems/decode-ways/
# 91. Decode Ways

# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6),
# or "BBF" (2 2 6).


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '0':
            return 0

        dp_m1 = None
        dp_m2 = None
        dp_next = None

        for i in range(len(s)):
            if i == 0:
                if int(s[i]) == 0:
                    return 0
                dp_next = 1
            else:
                num = int(str(s[i - 1]) + str(s[i]))
                if 0 < num <= 26:
                    dp_next = 0
                    if int(s[i]) != num:
                        dp_next += (dp_m2 if i >= 2 else 1)
                    if int(s[i]) != 0:
                        dp_next += dp_m1
                elif int(s[i]) != 0:
                    dp_next = dp_m1
                else:
                    return 0

            dp_m2 = dp_m1
            dp_m1 = dp_next

        return dp_next
