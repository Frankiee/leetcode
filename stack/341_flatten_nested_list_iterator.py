# [Classic, Nested-Iterator]
# https://leetcode.com/problems/flatten-nested-list-iterator/
# 341. Flatten Nested List Iterator

# History:
# Facebook
# 1.
# Apr 3, 2020
# 2.
# May 2, 2020
# 3.
# May 31, 2020

# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other
# lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,4,6].


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIteratorStack(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()

        ret, pt = self.stack[-1]
        self.stack[-1][1] += 1
        return ret[pt]

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nl, nl_pt = self.stack[-1]

            if nl_pt >= len(nl):
                self.stack.pop(-1)
            else:
                item = nl[nl_pt]

                if item.isInteger():
                    return True

                self.stack[-1][1] += 1
                self.stack.append([item.getList(), 0])

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIteratorPointer(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.nl_pt = 0

        self.buff = []
        self.buff_pt = 0

    def _flatten(self, nxt):
        if nxt.isInteger():
            return [nxt.getInteger()]
        else:
            ret = []

            for n in nxt.getList():
                ret.extend(self._flatten(n))

            return ret

    def _fill_buff(self):
        while self.buff_pt >= len(self.buff) and self.nl_pt < len(self.nestedList):
            nxt = self.nestedList[self.nl_pt]

            self.buff_pt = 0
            self.buff = self._flatten(nxt)

            self.nl_pt += 1

    def next(self):
        """
        :rtype: int
        """
        ret = self.buff[self.buff_pt]
        self.buff_pt += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        self._fill_buff()
        return self.buff_pt < len(self.buff)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
