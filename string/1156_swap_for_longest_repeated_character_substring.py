# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
# 1156. Swap For Longest Repeated Character Substring

# Given a string text, we are allowed to swap two of the characters in the
# string. Find the length of the longest substring with repeated characters.
#
#
# Example 1:
#
# Input: text = "ababa"
# Output: 3
# Explanation: We can swap the first 'b' with the last 'a', or the last 'b'
# with the first 'a'. Then, the longest repeated character substring is
# "aaa", which its length is 3.
# Example 2:
#
# Input: text = "aaabaaa"
# Output: 6
# Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get
# longest repeated character substring "aaaaaa", which its length is 6.
# Example 3:
#
# Input: text = "aaabbaaa"
# Output: 4
# Example 4:
#
# Input: text = "aaaaa"
# Output: 5
# Explanation: No need to swap, longest repeated character substring is
# "aaaaa", length is 5.
# Example 5:
#
# Input: text = "abcdef"
# Output: 1
#
#
# Constraints:
#
# 1 <= text.length <= 20000
# text consist of lowercase English characters only.


from collections import defaultdict


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        chars = defaultdict(list)

        c_char = None
        c_char_start = None
        for idx in range(len(text)):
            c = text[idx]
            if not c_char:
                c_char = c
                c_char_start = idx
            elif c != c_char:
                chars[c_char].append((c_char_start, idx - 1))
                c_char = c
                c_char_start = idx
        chars[c_char].append((c_char_start, len(text) - 1))

        max_len = float('-inf')
        for c, distri in chars.iteritems():
            for idx in range(len(distri)):
                if (idx < len(distri) - 1 and
                        distri[idx][1] == distri[idx + 1][0] - 2):
                    if len(distri) >= 3:
                        max_len = max(
                            max_len,
                            distri[idx + 1][1] - distri[idx][0] + 1,
                        )
                    else:  # len(distri) == 2
                        max_len = max(
                            max_len,
                            distri[idx + 1][1] - distri[idx][0],
                        )
                elif len(distri) > 1:
                    # Swap 1 item
                    max_len = max(
                        max_len,
                        distri[idx][1] - distri[idx][0] + 2,
                    )
                else:
                    # No swap
                    max_len = max(
                        max_len,
                        distri[idx][1] - distri[idx][0] + 1,
                    )

        return max_len
