# [Archived]
# https://leetcode.com/problems/goal-parser-interpretation/
# 1678. Goal Parser Interpretation

# History:
# 1.
# Apr 11, 2021

# You own a Goal Parser that can interpret a string command.
# The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.
#
# Given the string command, return the Goal Parser's interpretation of command.
#
#
#
# Example 1:
#
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:
#
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:
#
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
#
#
# Constraints:
#
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ret = []
        command_idx = 0

        while command_idx < len(command):
            if command[command_idx] == 'G':
                ret.append('G')
                command_idx += 1
            elif command[command_idx + 1] == 'a':
                ret.append('al')
                command_idx += 4
            else:
                ret.append('o')
                command_idx += 2

        return "".join(ret)
