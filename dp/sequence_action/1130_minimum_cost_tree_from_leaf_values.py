# [DP-Sequence-Action]
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# 1130. Minimum Cost Tree From Leaf Values

# Given an array arr of positive integers, consider all binary trees such that:
#
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order
# traversal of the tree.  (Recall that a node is a leaf if and only if it
# has 0 children.)
# The value of each non-leaf node is equal to the product of the largest
# leaf value in its left and right subtree respectively.
# Among all possible binary trees considered, return the smallest possible
# sum of the values of each non-leaf node.  It is guaranteed this sum fits
# into a 32-bit integer.
#
#
#
# Example 1:
#
# Input: arr = [6,2,4]
# Output: 32
# Explanation:
# There are two possible trees.  The first has non-leaf node sum 36, and the
# second has non-leaf node sum 32.
#
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4
#
#
# Constraints:
#
# 2 <= arr.length <= 40
# 1 <= arr[i] <= 15
# It is guaranteed that the answer fits into a 32-bit signed integer (ie. it
# is less than 2^31).


# WARNING: Better solution using stack exists

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0

        ret_dp = {}
        max_dp = {}

        for i in range(len(arr)):
            ret_dp[(i, i)] = 0

        for length in range(2, len(arr) + 1):
            for l in range(0, len(arr) - length + 1):
                r = l + length - 1
                for k in range(l, r):
                    if (l, k) in max_dp:
                        max_l_k = max_dp[(l, k)]
                    else:
                        max_l_k = max(
                            [arr[idx] for idx in range(l, k + 1)])
                        max_dp[(l, k)] = max_l_k

                    if (k + 1, r) in max_dp:
                        max_k_l_r = max_dp[(k + 1, r)]
                    else:
                        max_k_l_r = max(
                            [arr[idx] for idx in range(k + 1, r + 1)])
                        max_dp[(k + 1, r)] = max_k_l_r

                    new_dp = (
                        max_l_k * max_k_l_r +
                        ret_dp[(l, k)] +
                        ret_dp[(k + 1, r)]
                    )
                    if (l, r) not in ret_dp:
                        ret_dp[(l, r)] = new_dp
                    else:
                        ret_dp[(l, r)] = min(
                            ret_dp[(l, r)],
                            new_dp,
                        )

        return ret_dp[0, len(arr) - 1]
