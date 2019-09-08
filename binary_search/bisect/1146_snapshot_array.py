# [Bisect]
# https://leetcode.com/problems/snapshot-array/
# 1146. Snapshot Array

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


from collections import defaultdict


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.current_v = 0
        self.data = defaultdict(list)

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if not self.data[index]:
            self.data[index].append((self.current_v, val))
        elif self.data[index][-1][0] == self.current_v:
            self.data[index][-1] = (self.current_v, val)
        else:
            self.data[index].append((self.current_v, val))

    def snap(self):
        """
        :rtype: int
        """
        self.current_v += 1
        return self.current_v - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if not self.data[index]:
            return 0
        else:
            lst = self.data[index]

            if not lst:
                return 0

            idx = self._bisect(lst, snap_id)

            if idx >= len(lst):
                return lst[-1][1]
            elif idx == 0 and lst[0][0] > snap_id:
                return 0
            elif lst[idx][0] > snap_id:
                return lst[idx - 1][1]
            else:
                return lst[idx][1]

    def _bisect(self, lst, snap_id):
        l = 0
        r = len(lst)

        while l < r:
            m = l + (r - l) / 2
            if lst[m][0] == snap_id:
                return m
            elif lst[m][0] > snap_id:
                r = m
            else:
                l = m + 1

        return l

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
