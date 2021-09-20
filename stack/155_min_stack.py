# https://leetcode.com/problems/min-stack/
# 155. Min Stack

# History:
# 1.
# May 20, 2019
# 2.
# Nov 24, 2019
# 3.
# May 5, 2020
# 4.
# Sep 18, 2021

# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack_pos = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.min_stack_pos.append(0)
        elif val < self.stack[self.min_stack_pos[-1]]:
            self.min_stack_pos.append(len(self.stack))

        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None

        if self.min_stack_pos and self.min_stack_pos[-1] == len(self.stack) - 1:
            self.min_stack_pos.pop()

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None

        return self.stack[self.min_stack_pos[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        new_min = min(x, self.min_stack[-1]) if self.stack else x
        self.stack.append(x)
        self.min_stack.append(new_min)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
