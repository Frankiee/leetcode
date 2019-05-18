# https://docs.google.com/spreadsheets/d/1MDAhN1RX6W6XhHbB-A62vmYma9FwcR3wwqzlT5ieV0g/edit#gid=0
# 187. Repeated DNA Sequences

# All DNA is composed of a series of nucleotides abbreviated as A, C, G,
# and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes
# useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule.
#
# Example:
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 11:
            return []

        dic = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3,
        }

        appear = set()
        repeat = set()

        val = 0
        for i in range(10):
            c_code = dic[s[i]]
            val = val << 2
            val |= c_code
        appear.add(val)

        for i in range(10, len(s)):
            c_code = dic[s[i]]
            val &= ~(3 << 18)
            val = val << 2
            val |= c_code

            if val in appear:
                repeat.add(s[i - 9:i + 1])
            else:
                appear.add(val)

        return list(repeat)
