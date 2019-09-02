# [Archived]
# https://leetcode.com/problems/summary-ranges/
# 228. Summary Ranges

# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        interval_start = None
        previous_num = None
        ret = []
        for n in nums:
            if interval_start is None:
                interval_start = n
            elif n != previous_num + 1:
                if previous_num == interval_start:
                    ret.append(str(interval_start))
                else:
                    ret.append("{}->{}".format(interval_start, previous_num))
                interval_start = n

            previous_num = n

        if previous_num == interval_start:
            ret.append(str(interval_start))
        else:
            ret.append("{}->{}".format(interval_start, previous_num))

        return ret
