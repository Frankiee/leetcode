# [Backtracking, Classic]
# https://leetcode.com/problems/longest-absolute-file-path/
# 388. Longest Absolute File Path

# History:
# Facebook
# 1.
# Jan 23, 2020
# 2.
# Apr 12, 2020
# 3.
# May 12, 2020

# Suppose we abstract our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2
# containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t
# \tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file
# file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level
# sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within
# our file system. For example, in the second example above, the longest absolute path is
# "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the
# longest absolute path to file in the abstracted file system. If there is no file in the system,
# return 0.
#
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
#
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path
# aaaaaaaaaaaaaaaaaaaaa/sth.png.


class Solution1(object):
    def _dfs(self, files, i, curr_len, curr):
        path = files[i]
        file_data = path.split('\t')
        file_name = file_data[-1]
        level = len(file_data) - 1

        while len(curr) > level:
            last = curr.pop(-1)
            curr_len -= len(last)
            if curr:
                curr_len -= 1

        if curr:
            curr_len += 1
        curr_len += len(file_name)
        curr.append(file_name)

        if '.' in file_name:
            self.max_length = max(self.max_length, curr_len)

        if i + 1 < len(files):
            self._dfs(files, i + 1, curr_len, curr)

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        files = input.split('\n')

        self.max_length = 0
        self._dfs(files, 0, 0, [])

        return self.max_length


class Solution2(object):
    def _dfs(self, paths, paths_idx, curr_longest, curr_length, curr_paths):
        if paths_idx == len(paths):
            return curr_longest

        nxt_path = paths[paths_idx].split('\t')
        levels = len(nxt_path) - 1
        nxt_path = nxt_path[-1]

        while len(curr_paths) > levels:
            curr_length -= curr_paths.pop(-1)
            if curr_paths:
                curr_length -= 1

        if curr_paths:
            curr_length += 1
        curr_paths.append(len(nxt_path))
        curr_length += len(nxt_path)

        if '.' in nxt_path:
            curr_longest = max(curr_longest, curr_length)

        return self._dfs(paths, paths_idx + 1, curr_longest, curr_length, curr_paths)

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split('\n')

        return self._dfs(paths, 0, 0, 0, [])
