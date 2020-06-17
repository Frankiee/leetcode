# [Backtracking, Classic]
# https://leetcode.com/problems/expression-add-operators/
# 282. Expression Add Operators

# History:
# Facebook
# 1.
# Jan 23, 2020
# 2.
# Apr 1, 2020
# 3.
# May 10, 2020

# Given a string that contains only digits 0-9 and a target value, return all possibilities to
# add binary operators (not unary) +, -, or * between the digits so they evaluate to the target
# value.
#
# Example 1:
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
# Example 2:
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# Example 3:
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
# Example 5:
#
# Input: num = "3456237490", target = 9191
# Output: []


class Solution(object):
    def dfs(self, num, target, curr_idx, curr_result, prev_num, curr_str, ret):
        if curr_idx >= len(num):
            if curr_result == target:
                ret.append(curr_str)
            return

        for idx in range(curr_idx + 1, len(num) + 1):
            new_num_str = num[curr_idx:idx]
            new_num = int(new_num_str)
            if idx == curr_idx + 1 or new_num_str[0] != '0':
                # +
                self.dfs(num, target, idx, curr_result + new_num, new_num,
                         curr_str + '+' + new_num_str, ret)
                # -
                self.dfs(num, target, idx, curr_result - new_num, -new_num,
                         curr_str + '-' + new_num_str, ret)
                # *
                self.dfs(num, target, idx, curr_result - prev_num + prev_num * new_num,
                         prev_num * new_num, curr_str + '*' + new_num_str, ret)

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []

        for idx in range(1, len(num) + 1):
            new_num_str = num[:idx]
            curr_result = int(new_num_str)
            if idx == 1 or new_num_str[0] != '0':
                self.dfs(num, target, idx, curr_result, curr_result, num[:idx], ret)

        return ret
