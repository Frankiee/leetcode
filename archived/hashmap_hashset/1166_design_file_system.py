# [Archived]
# https://leetcode.com/problems/design-file-system/
# 1166. Design File System

# history
# Airbnb
# 1.
# Oct 17, 2020

# You are asked to design a file system that allows you to create new paths and associate them with different values.
#
# The format of a path is one or more concatenated strings of the form:
# / followed by one or more lowercase English letters.
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.
#
# Implement the FileSystem class:
#
# bool createPath(string path, int value)
# Creates a new path and associates a value to it if possible and returns true.
# Returns false if the path already exists or its parent path doesn't exist.
# int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
#
#
# Example 1:
#
# Input:
# ["FileSystem","createPath","get"]
# [[],["/a",1],["/a"]]
# Output:
# [null,true,1]
# Explanation:
# FileSystem fileSystem = new FileSystem();
#
# fileSystem.createPath("/a", 1); // return true
# fileSystem.get("/a"); // return 1
# Example 2:
#
# Input:
# ["FileSystem","createPath","createPath","get","createPath","get"]
# [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
# Output:
# [null,true,true,2,false,-1]
# Explanation:
# FileSystem fileSystem = new FileSystem();
#
# fileSystem.createPath("/leet", 1); // return true
# fileSystem.createPath("/leet/code", 2); // return true
# fileSystem.get("/leet/code"); // return 2
# fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
# fileSystem.get("/c"); // return -1 because this path doesn't exist.
#
#
# Constraints:
#
# The number of calls to the two functions is less than or equal to 104 in total.
# 2 <= path.length <= 100
# 1 <= value <= 109

class FileSystem(object):

    def __init__(self):
        self.mem = {}

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        parent_path = "/".join(path.split('/')[:-1])

        if path not in self.mem and (parent_path == "" or parent_path in self.mem):
            self.mem[path] = value
            return True

        return False

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        return self.mem.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
