# [Bisect-Lower-Bound, Classic]
# https://leetcode.com/problems/exam-room/
# 855. Exam Room

# History:
# 1.
# Mar 7, 2020
# 2.
# May 11, 2020

# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
#
# When a student enters the room, they must sit in the seat that maximizes the distance to the
# closest person.  If there are multiple such seats, they sit in the seat with the lowest number.
# (Also, if no one is in the room, then the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int
# representing what seat the student sat in, and ExamRoom.leave(int p) representing that the
# student in seat number p now leaves the room.  It is guaranteed that any calls to
# ExamRoom.leave(p) have a student sitting in seat p.
#
#
#
# Example 1:
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# ​​​​​​​
#
# Note:
#
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.seats = []
        self.N = N

    def _bisect_seats(self, pos):
        l, r = 0, len(self.seats)

        while l < r:
            m = (r - l) / 2 + l

            if self.seats[m] >= pos:
                r = m
            else:
                l = m + 1

        return l

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seats) == 0:
            self.seats.append(0)
            return 0

        max_insert_pos = None
        max_pos = None
        max_space = float('-inf')
        for i in range(len(self.seats)):
            if i == 0:
                space = self.seats[0] - 1
                pos = 0
                insert_pos = 0
            else:
                space = (self.seats[i] - self.seats[i - 1] - 2) / 2
                pos = (self.seats[i] + self.seats[i - 1]) / 2
                insert_pos = i

            if space > max_space:
                max_space = space
                max_pos = pos
                max_insert_pos = insert_pos

        if self.N - 2 - self.seats[-1] > max_space:
            max_space = self.N - 2 - self.seats[-1]
            max_pos = self.N - 1
            max_insert_pos = len(self.seats)

        self.seats.insert(max_insert_pos, max_pos)

        return max_pos

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        pos = self._bisect_seats(p)
        self.seats.pop(pos)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
