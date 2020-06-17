# https://leetcode.com/problems/design-compressed-string-iterator/
# 604. Design Compressed String Iterator

# History:
# Google
# 1.
# Mar 13, 2020

# Design and implement a data structure for a compressed string iterator. It should support the
# following operations: next and hasNext.
#
# The given compressed string will be in the form of each letter followed by a positive integer
# representing the number of this letter existing in the original uncompressed string.
#
# next() - if the original string still has uncompressed characters, return the next letter;
# Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#
# Note:
# Please remember to RESET your class variables declared in StringIterator, as static/class
# variables are persisted across multiple test cases. Please see here for more details.
#
# Example:
#
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
#
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.str = compressedString
        self.pos = 0
        self.buff_char = None
        self.buff_chat_left = 0

    def next(self):
        """
        :rtype: str
        """
        if self.buff_chat_left > 0:
            self.buff_chat_left -= 1
            return self.buff_char

        if self.pos >= len(self.str):
            return ' '

        self.buff_char = self.str[self.pos]
        self.pos += 1
        while self.pos < len(self.str) and self.str[self.pos].isdigit():
            self.buff_chat_left *= 10
            self.buff_chat_left += int(self.str[self.pos])
            self.pos += 1

        self.buff_chat_left -= 1
        return self.buff_char

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.buff_chat_left != 0 or self.pos != len(self.str)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
