# [DP-Array-Subsequence]
# https://leetcode.com/discuss/interview-question/661336/Google-or-Onsite-or-Count-Increasing-Subsequences
# Count Increasing Subsequences

# History:
# Google
# 1.
# Jun 15, 2020

# Given an array arr of size n. Find the number of triples (i, j, k) where:
#
# i < j < k
# arr[i] < arr[j] < arr[k]
# Example 1:
#
# Input: arr = [1, 2, 3, 4, 5]
# Output: 10
# Explanation:
# 1. 1 2 3
# 2. 1 2 4
# 3. 1 2 5
# 4. 1 3 4
# 5. 1 3 5
# 6. 1 4 5
# 7. 2 3 4
# 8. 2 3 5
# 9. 2 4 5
# 10. 3 4 5
# Example 2:
#
# Input: arr = [1, 2, 3, 5, 4]
# Output: 7
# Example 3:
#
# Input: arr = [5, 4, 3, 2, 1]
# Output: 0
# Follow-up:
# Count number of increasing subsequences in the array arr of size k.
#
# Example 1:
#
# Input: arr = [1, 2, 3, 4, 5], k = 4
# Output: 5
# Explanation:
# 1. 1 2 3 4
# 2. 1 2 3 5
# 3. 1 2 4 5
# 4. 1 3 4 5
# 5. 2 3 4 5


class Solution(object):
    def count_increasing_sequences(self, arr, k):
        dp = [1] * len(arr)

        for _ in range(2, k + 1):
            nxt_dp = [0] * len(arr)
            for r_i, n in enumerate(arr):
                for l_i in range(r_i):
                    if arr[r_i] > arr[l_i]:
                        nxt_dp[r_i] += dp[l_i]
            dp = nxt_dp

        return sum(dp)


solution = Solution()
print solution.count_increasing_sequences([1, 2, 3, 4, 5], 3)
