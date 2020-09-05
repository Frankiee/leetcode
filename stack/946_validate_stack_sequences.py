# https://leetcode.com/problems/validate-stack-sequences/
# 946. Validate Stack Sequences

# History:
# Google
# 1.
# Mar 11, 2020
# 2.
# Apr 28, 2020
# 3.
# Jun 23, 2020

# Given two sequences pushed and popped with distinct values, return true if and only if this
# could have been the result of a sequence of push and pop operations on an initially empty stack.
#
#
#
# Example 1:
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
# Note:
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.


class SolutionConstantSpace(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack_pt = -1

        pop_pt = 0
        for read_pt in range(len(pushed)):
            stack_pt += 1
            pushed[stack_pt] = pushed[read_pt]
            while stack_pt >= 0 and pop_pt >= 0 and pushed[stack_pt] == popped[pop_pt]:
                stack_pt -= 1
                pop_pt += 1

            if stack_pt == -1 and pop_pt == len(popped):
                return True

            if pop_pt == len(popped):
                return False

        return stack_pt == -1 and pop_pt == len(popped)


class SolutionStack(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []

        pop_idx = 0
        for push_idx, p in enumerate(pushed):
            stack.append(p)
            while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
                stack.pop(-1)
                pop_idx += 1

        return not bool(stack)
