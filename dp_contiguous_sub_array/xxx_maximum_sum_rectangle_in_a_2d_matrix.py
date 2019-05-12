# https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/
# Maximum Sum Rectangle in a 2D Matrix

# Given a 2D array, find the maximum sum subarray in it.
# For example, in the following 2D array, the maximum sum subarray is
# highlighted with blue rectangle and sum of this subarray is 29

# [
#     [1, 2, -1, -4, -20],
#     [-8, -3, 4, 2, 1],
#     [3, 8, 10, 1, 3],
#     [-4, -1, 1, 7, -6],
# ]


class Solution(object):
    def __init__(self):
        self.curr_array = []

    def max_subarray(self):
        dp = float('-inf')
        max_so_far = float('-inf')

        for i in self.curr_array:
            dp = i if dp < 0 else i + dp
            max_so_far = max(max_so_far, dp)

        return max_so_far

    def maxSumRectangle(self, matrix):
        max_so_far = float('-inf')

        for l in range(len(matrix[0])):
            self.curr_array = []
            for r in range(l, len(matrix[0])):
                if not self.curr_array:
                    for c in range(len(matrix)):
                        self.curr_array.append(matrix[c][r])
                else:
                    for c in range(len(matrix)):
                        self.curr_array[c] += matrix[c][r]

                max_so_far = max(
                    max_so_far,
                    self.max_subarray()
                )

        return max_so_far


s = Solution()
print s.maxSumRectangle(
    [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]
)
