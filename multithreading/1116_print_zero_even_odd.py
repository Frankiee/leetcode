# [Important]
# https://leetcode.com/problems/print-zero-even-odd/
# 1116. Print Zero Even Odd

# Suppose you are given the following code:
#
# class ZeroEvenOdd {
#   public ZeroEvenOdd(int n) { ... }      // constructor
#   public void zero(printNumber) { ... }  // only output 0's
#   public void even(printNumber) { ... }  // only output even numbers
#   public void odd(printNumber) { ... }   // only output odd numbers
# }
# The same instance of ZeroEvenOdd will be passed to three different threads:
#
# Thread A will call zero() which should only output 0's.
# Thread B will call even() which should only ouput even numbers.
# Thread C will call odd() which should only output odd numbers.
# Each of the threads is given a printNumber method to output an integer.
# Modify the given program to output the series 010203040506... where the
# length of the series must be 2n.
#
#
# Example 1:
#
# Input: n = 2
# Output: "0102"
# Explanation: There are three threads being fired asynchronously. One of
# them calls zero(), the other calls even(), and the last one calls odd().
# "0102" is the correct output.
#
# Example 2:
#
# Input: n = 5
# Output: "0102030405"

from threading import Lock


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.non_zero_lock = Lock()
        self.non_zero_lock.acquire()
        self.odd_lock = Lock()
        self.even_lock = Lock()
        self.even_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.zero_lock.acquire()

            printNumber(0)

            self.non_zero_lock.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n / 2):
            self.even_lock.acquire()
            self.non_zero_lock.acquire()

            printNumber((i + 1) * 2)

            self.odd_lock.release()
            self.zero_lock.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range((self.n + 1) / 2):
            self.odd_lock.acquire()
            self.non_zero_lock.acquire()

            printNumber(i * 2 + 1)

            self.even_lock.release()
            self.zero_lock.release()
