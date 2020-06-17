# [Bisect-Lower-Bound]
# https://leetcode.com/problems/snapshot-array/
# 1146. Snapshot Array

# History:
# Facebook
# 1.
# Mar 3, 2020

# Implement a SnapshotArray that supports the following interface:
#
# SnapshotArray(int length) initializes an array-like data structure with
# the given length.  Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the
# total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time
# we took the snapshot with the given snap_id
#
#
# Example 1:
#
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation:
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0,
# return 5
#
#
# Constraints:
#
# 1 <= length <= 50000
# At most 50000 calls will be made to set, snap, and get.
# 0 <= index < length
# 0 <= snap_id < (the total number of times we call snap())
# 0 <= val <= 10^9


import bisect


class SnapshotArrayBisect(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.mem = [[[0, 0]] for _ in range(length)]
        self.curr_version = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.mem[index][-1][0] == self.curr_version:
            self.mem[index][-1] = [self.curr_version, val]
        else:
            self.mem[index].append([self.curr_version, val])

    def snap(self):
        """
        :rtype: int
        """
        self.curr_version += 1
        return self.curr_version - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        i = bisect.bisect(self.mem[index], [snap_id+1]) - 1
        return self.mem[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.mem = [[[0, 0]] for _ in range(length)]
        self.curr_version = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.mem[index][-1][0] == self.curr_version:
            self.mem[index][-1] = [self.curr_version, val]
        else:
            self.mem[index].append([self.curr_version, val])

    def snap(self):
        """
        :rtype: int
        """
        self.curr_version += 1
        return self.curr_version - 1

    def _bisect(self, search_arry, snap_id):
        l, r = 0, len(search_arry)

        while l < r:
            m = (r - l) / 2 + l

            if search_arry[m][0] == snap_id:
                return m
            elif search_arry[m][0] > snap_id:
                r = m - 1
            else:
                l = m

        return l

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        search_arry = self.mem[index]

        i = self._bisect(search_arry, snap_id)

        return self.mem[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
