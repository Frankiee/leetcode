# https://leetcode.com/problems/decode-string/
# 394. Decode String

# History:
# Facebook
# 1.
# Mar 3, 2020
# 2.
# Mar 31, 2020
# 3.
# Apr 30, 2020

# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is
# being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets
# are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits
# are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '[':
                stack.append(num)
                stack.append(c)
                num = 0
            elif c.isalpha():
                stack.append(c)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop(-1))

                stack.pop(-1)
                count = stack.pop(-1)
                stack.extend(count * temp[::-1])

        return "".join(stack)


class SolutionNestedList(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        repeats = 0

        for c in s:
            if c.isdigit():
                repeats *= 10
                repeats += int(c)
            elif c == '[':
                stack.append(repeats)
                stack.append([])
                repeats = 0
            elif c == ']':
                strings = stack.pop(-1)
                count = stack.pop(-1)
                if len(stack) > 0 and isinstance(stack[-1], list):
                    stack[-1].extend(strings * count)
                else:
                    stack.extend(strings * count)
            else:
                if len(stack) > 0 and isinstance(stack[-1], list):
                    stack[-1].append(c)
                else:
                    stack.append(c)

        return "".join(stack)
