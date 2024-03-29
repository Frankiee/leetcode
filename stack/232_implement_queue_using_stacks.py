# https://leetcode.com/problems/implement-queue-using-stacks/
# 232. Implement Queue using Stacks

# History:
# 1.
# May 20, 2019
# 2.
# Nov 12, 2019

# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Example:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# Notes:
#
# You must use only standard operations of a stack -- which means only push
# to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.out_stack, self.in_stack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def _move(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.out_stack:
            self._move()

        return self.out_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out_stack:
            self._move()

        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.out_stack and not self.in_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
