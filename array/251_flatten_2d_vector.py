# https://leetcode.com/problems/flatten-2d-vector/
# 251. Flatten 2D Vector

# History:
# Facebook
# 1.
# Mar 27, 2020
# 2.
# Apr 13. 2020

# Design and implement an iterator to flatten a 2d vector. It should support the following
# operations: next and hasNext.
#
#
#
# Example:
#
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
#
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
#
#
# Notes:
#
# Please remember to RESET your class variables declared in Vector2D, as static/class variables
# are persisted across multiple test cases. Please see here for more details.
# You may assume that next() call will always be valid, that is, there will be at least a next
# element in the 2d vector when next() is called.
#
#
# Follow up:1060
#
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.p1 = 0
        self.p2 = 0

    def _forward(self):
        while not (self.p1 < len(self.v) and self.p2 < len(self.v[self.p1])):
            self.p1 += 1
            self.p2 = 0

            if self.p1 >= len(self.v):
                return

    def next(self):
        """
        :rtype: int
        """
        self._forward()

        ret = self.v[self.p1][self.p2]
        self.p2 += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        self._forward()

        return self.p1 < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
