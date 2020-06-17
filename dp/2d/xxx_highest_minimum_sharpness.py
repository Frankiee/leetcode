# https://www.1point3acres.com/bbs/interview/dropbox-software-engineer-307965.html
# Highest Minimum Sharpness

# History:
# Dropbox
# 1.
# Feb 27, 2020

# Given a 2-d array of "sharpness" values. Find a path from the leftmost column to the rightmost
# column which has the highest minimum sharpness.
# Output the highest minimum sharpness. Each move can only move to the top right, right or
# bottom right grid.
#
# Example: 3*3 matrix
# 5 7 2
# 7 5 8
# 9 1 5
# The path with highest minimum sharpness is 7-->7-->8, because 7 is the highest minimum value
# in all the paths.


class Solution(object):
    def highestMinimumSharpness(self, matrix):
        if not matrix or not matrix[0]:
            return None

        dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                max_pre = None

                if c > 0:
                    max_pre = dp[r][c-1]
                    if r > 0:
                        max_pre = max(dp[r-1][c-1], max_pre)
                    if r < len(matrix) - 1:
                        max_pre = max(dp[r+1][c-1], max_pre)

                dp[r][c] = min(matrix[r][c], max_pre) if max_pre else matrix[r][c]

        return max([dp[r][-1] for r in range(len(matrix))])


s = Solution()

matrix = [
    [5, 7, 2],
    [7, 5, 8],
    [9, 1, 5],
]
print s.highestMinimumSharpness(matrix)
