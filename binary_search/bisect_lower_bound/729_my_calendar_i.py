# [Bisect-Lower-Bound]
# https://leetcode.com/problems/my-calendar-i/
# 729. My Calendar I

# History:
# Google
# 1.
# Mar 24, 2020
# 2.
# Jun 14, 2020

# Implement a MyCalendar class to store your events. A new event can be
# added if adding the event will not cause a double booking.
#
# Your class will have the method, book(int start, int end). Formally,
# this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
#
# A double booking happens when two events have some non-empty intersection
# (ie., there is some time that is common to both events.)
#
# For each call to the method MyCalendar.book, return true if the event can
# be added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar();
# MyCalendar.book(start, end)
# Example 1:
#
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is
# already booked by another event.
# The third event can be booked, as the first event takes every time less
# than 20, but not including 20.
#
#
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the
# range [0, 10^9].


# O(log(n) for book
class TreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendarTree(object):

    def __init__(self):
        self.root = None

    def _insert_into_tree(self, node, curr_node):
        if not curr_node:
            return True, node

        if node.start >= curr_node.end:
            success, new_right_node = self._insert_into_tree(node, curr_node.right)
            if not success:
                return False, None

            curr_node.right = new_right_node
            return True, curr_node
        elif node.end <= curr_node.start:
            success, new_left_node = self._insert_into_tree(node, curr_node.left)
            if not success:
                return False, None

            curr_node.left = new_left_node
            return True, curr_node
        else:
            return False, None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        node = TreeNode(start, end)

        success, node = self._insert_into_tree(node, self.root)
        if not self.root:
            self.root = node
        return success


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# O(n) for book
class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def bisect(self, num):
        l = 0
        r = len(self.calendar)

        while l < r:
            m = l + (r - l) / 2

            if num <= self.calendar[m][0]:
                r = m
            else:
                l = m + 1

        return l

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = self.bisect(start)

        if ((i < len(self.calendar) and end > self.calendar[i][0]) or
                (i > 0 and start < self.calendar[i - 1][1])):
            return False

        self.calendar.insert(i, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


class MyCalendarCompareEnd(object):

    def __init__(self):
        self.bookings = []

    def _bisect(self, start, end):
        l, r = 0, len(self.bookings)

        while l < r:
            m = (r - l) / 2 + l

            if self.bookings[m][0] >= end:
                r = m
            else:
                l = m + 1

        return l

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        insertion_pos = self._bisect(start, end)

        if insertion_pos == 0 or self.bookings[insertion_pos - 1][1] <= start:
            self.bookings.insert(insertion_pos, (start, end))
            return True

        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
