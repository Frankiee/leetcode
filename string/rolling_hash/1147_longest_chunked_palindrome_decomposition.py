# [Rolling-Hash, Classic]
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# 1147. Longest Chunked Palindrome Decomposition

# Return the largest possible k such that there exists a_1, a_2, ...,
# a_k such that:
#
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.
#
#
# Example 1:
#
# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(
# hello)(abcdef)(ghi)".
# Example 2:
#
# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".
# Example 3:
#
# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(
# pre)(a)(nt)(a)".
# Example 4:
#
# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".
#
#
# Constraints:
#
# text consists only of lowercase English characters.
# 1 <= text.length <= 1000


class Solution(object):
    def _to_idx(self, c):
        return ord(c) - ord('a') + 1

    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        if not text:
            return 0

        if len(text) == 1:
            return 1

        ret = 0

        l = -1
        r = len(text)

        rolling_hash_key = 26

        l_hash = 0
        r_hash = 0
        rolling_len = 0

        while l < r:
            l += 1
            r -= 1

            if l == r:
                ret += 1
                return ret
            elif l > r:
                if rolling_len > 0:
                    ret += 1
                return ret

            l_hash = l_hash * rolling_hash_key + self._to_idx(text[l])
            r_hash += self._to_idx(text[r]) * rolling_hash_key ** rolling_len

            rolling_len += 1

            if l_hash == r_hash:
                ret += 2

                l_hash = 0
                r_hash = 0
                rolling_len = 0
