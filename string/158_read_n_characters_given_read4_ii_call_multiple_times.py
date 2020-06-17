# [Classic]
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/
# 158. Read N Characters Given Read4 II - Call multiple times

# History:
# Facebook
# 1.
# Apr 12, 2020
# 2.
# Apr 14, 2020
# 3.
# May 12, 2020

# Given a file and assume that you can only read the file using a given method read4, implement a
# method read to read n characters. Your method read may be called multiple times.
#
#
#
# Method read4:
#
# The API read4 reads 4 consecutive characters from the file, then writes those characters into
# the buffer array buf.
#
# The return value is the number of actual characters read.
#
# Note that read4() has its own file pointer, much like FILE *fp in C.
#
# Definition of read4:
#
#     Parameter:  char[] buf
#     Returns:    int
#
# Note: buf[] is destination not source, the results from read4 will be copied to buf[]
# Below is a high level example of how read4 works:
#
# File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
# char[] buf = new char[4]; // Create buffer with enough space to store characters
# read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
# read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
# read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file
#
#
# Method read:
#
# By using the read4 method, implement the method read that reads n characters from the file and
# store it in the buffer array buf. Consider that you cannot manipulate the file directly.
#
# The return value is the number of actual characters read.
#
# Definition of read:
#
#     Parameters:	char[] buf, int n
#     Returns:	int
#
# Note: buf[] is destination not source, you will need to write the results to buf[]
#
#
# Example 1:
#
# File file("abc");
# Solution sol;
# // Assume buf is allocated and guaranteed to have enough space for storing all characters from
# the file.
# sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of
# 1 character from the file, so return 1.
# sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the
# file, so return 2.
# sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
# Example 2:
#
# File file("abc");
# Solution sol;
# sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total
# of 3 characters from the file, so return 3.
# sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
#
#
# Note:
#
# Consider that you cannot manipulate the file directly, the file is only accesible for read4 but
# not for read.
# The read function may be called multiple times.
# Please remember to RESET your class variables declared in Solution, as static/class variables
# are persisted across multiple test cases. Please see here for more details.
# You may assume the destination buffer array, buf, is guaranteed to have enough space for
# storing n characters.
# It is guaranteed that in a given test case the same buffer buf is called by read.


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


# The read4 API is already defined for you.
# @param buf, List[str]
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self, ):
        self.read4_buff = [' '] * 4
        self.read4_buff_idx = 0
        self.read4_count = 0

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        curr_buf_idx = 0
        while curr_buf_idx < n and self.read4_buff_idx < self.read4_count:
            buf[curr_buf_idx] = self.read4_buff[self.read4_buff_idx]
            curr_buf_idx += 1
            self.read4_buff_idx += 1

            if curr_buf_idx == n:
                return curr_buf_idx

        while curr_buf_idx < n:
            self.read4_count = read4(self.read4_buff)
            self.read4_buff_idx = 0

            while curr_buf_idx < n and self.read4_buff_idx < self.read4_count:
                buf[curr_buf_idx] = self.read4_buff[self.read4_buff_idx]
                curr_buf_idx += 1
                self.read4_buff_idx += 1

                if curr_buf_idx == n:
                    return curr_buf_idx

            if self.read4_count < 4:
                return curr_buf_idx

        return curr_buf_idx


"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution2(object):
    def __init__(self):
        self.read4_buf = [None] * 4
        self.read4_count = 0
        self.read4_i = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while self.read4_i < self.read4_count and i < n:
            buf[i] = self.read4_buf[self.read4_i]
            i += 1
            self.read4_i += 1

        while i < n:
            self.read4_count = read4(self.read4_buf)
            self.read4_i = 0

            while self.read4_i < self.read4_count and i < n:
                buf[i] = self.read4_buf[self.read4_i]
                i += 1
                self.read4_i += 1

            if self.read4_count < 4:
                return i

        return i
