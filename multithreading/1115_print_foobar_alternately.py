# https://leetcode.com/problems/print-foobar-alternately/
# 1115. Print FooBar Alternately

# History:
# 1.
# Aug 10, 2019
# 2.
# Mar 31, 2020

# Suppose you are given the following code:
#
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
#
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
# The same instance of FooBar will be passed to two different threads.
# Thread A will call foo() while thread B will call bar(). Modify the given
# program to output "foobar" n times.
#
#
#
# Example 1:
#
# Input: n = 1
# Output: "foobar"
# Explanation: There are two threads being fired asynchronously. One of them
# calls foo(), while the other calls bar(). "foobar" is being output 1 time.
# Example 2:
#
# Input: n = 2
# Output: "foobarfoobar"
# Explanation: "foobar" is being output 2 times.

from threading import Lock


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.foo_lock.acquire()

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.bar_lock.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.bar_lock.acquire()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.foo_lock.release()


from threading import Condition


# Python 3
class FooBarConditionalVariable:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()

        self.foo_counter = 0
        self.bar_counter = 0

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.cv:
                self.cv.wait_for(lambda: self.foo_counter == self.bar_counter)
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()

                self.foo_counter += 1
                self.cv.notify(1)

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            with self.cv:
                self.cv.wait_for(lambda: self.foo_counter > self.bar_counter)
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()

                self.bar_counter += 1
                self.cv.notify(1)
