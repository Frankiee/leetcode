# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/submissions/
# 698. Partition to K Equal Sum Subsets

# Related:
# 416. Partition Equal Subset Sum

# Given an array of integers nums and a positive integer k, find whether
# it's possible to divide this array into k non-empty subsets whose sums are
# all equal.
#
#
# Example 1:
#
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
# Note:
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

# Note:
# 1, if remainings[s_idx] == goal: break
#
# The key is, remainings[s_idx] == goal means for all k > s_idx,
# remainings[k] == goal; because this algorithm always fill the previous
# buckets before trying the next.
# So if by putting nums[i] in this empty bucket can't solve the game,
# putting nums[i] on other empty buckets can't solve the game either.
#
# 2, nums.sort(reverse=True)
#
# Always start from big numbers for this kind of problem, just by doing it
# yourself for a few times you will find out that the big numbers are the
# easiest to place.


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)
        if total % k != 0:
            return False

        goal = total / k

        if any([n > goal for n in nums]):
            return False

        nums.sort(reverse=True)
        remainings = [goal] * k

        def dfs(idx):
            if idx >= len(nums):
                return all([s == 0 for s in remainings])

            current_n = nums[idx]

            for s_idx in range(len(remainings)):
                s = remainings[s_idx]
                if s >= current_n:
                    remainings[s_idx] -= current_n
                    if dfs(idx + 1):
                        return True
                    remainings[s_idx] += current_n

                    if remainings[s_idx] == goal:
                        break

            return False

        return dfs(0)
