# https://leetcode.com/problems/two-sum-iii-data-structure-design/
# 170. Two Sum III - Data structure design

# History:
# 1.
# Jul 22, 2021

# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up
# to a particular value.
#
# Implement the TwoSum class:
#
# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value,
# otherwise, it returns false.
#
#
# Example 1:
#
# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]
#
# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return true
# twoSum.find(7);  // No two integers sum up to 7, return false
#
#
# Constraints:
#
# -105 <= number <= 105
# -231 <= value <= 231 - 1
# At most 5 * 104 calls will be made to add and find.

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.mem:
            self.mem[number] += 1
        else:
            self.mem[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.mem:
            expect = value - n
            if expect == n:
                if n in self.mem and self.mem[n] > 1:
                    return True
            else:
                if expect in self.mem and self.mem[expect] > 0:
                    return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
