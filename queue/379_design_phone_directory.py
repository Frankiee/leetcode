# https://leetcode.com/problems/design-phone-directory/
# 379. Design Phone Directory

# History:
# Dropbox
# 1.
# Feb 22, 2020

# Design a Phone Directory which supports the following operations:
#
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.recycled = set()
        self.next = 0
        self.max_num = maxNumbers

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.recycled:
            return self.recycled.pop()
        if self.next < self.max_num:
            self.next += 1
            return self.next -1
        return -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.recycled or self.next <= number < self.max_num

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number < self.next:
            self.recycled.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
