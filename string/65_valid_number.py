# [Classic]
# https://leetcode.com/problems/valid-number/
# 65. Valid Number

# History:
# Facebook
# 1.
# Apr 3, 2020
# 2.
# May 12, 2020

# Validate if a given string can be interpreted as a decimal number.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# Note: It is intended for the problem statement to be ambiguous. You should gather all
# requirements up front before implementing one. However, here is a list of characters that can
# be in a valid decimal number:
#
# Numbers 0-9
# Exponent - "e"
# Positive/negative sign - "+"/"-"
# Decimal point - "."
# Of course, the context of these characters also matters in the input.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature
# accepts a const char * argument, please click the reload button to reset your code definition.


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        e_seen = False
        num_seen = False
        dot_seen = False
        num_after_e = False

        for idx, c in enumerate(s):
            if c.isdigit():
                num_seen = True
                if e_seen:
                    num_after_e = True
            elif c == 'e':
                if e_seen or not num_seen:
                    return False
                e_seen = True
            elif c in {'+', '-'}:
                if idx != 0 and s[idx - 1] != 'e':
                    return False
            elif c == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            else:
                return False

        return num_seen and (not e_seen or num_after_e)
