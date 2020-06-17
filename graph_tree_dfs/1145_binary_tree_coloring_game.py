# [Classic, Game-Play]
# https://leetcode.com/problems/binary-tree-coloring-game/
# 1145. Binary Tree Coloring Game

# History:
# Facebook
# 1.
# Mar 30, 2020

# Two players play a turn based game on a binary tree.  We are given the root of this binary
# tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from
# 1 to n.
#
# Initially, the first player names a value x with 1 <= x <= n, and the second player names a
# value y with 1 <= y <= n and y != x.  The first player colors the node with value x red,
# and the second player colors the node with value y blue.
#
# Then, the players take turns starting with the first player.  In each turn, that player chooses
# a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of
# the chosen node (either the left child, right child, or parent of the chosen node.)
#
# If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If
# both players pass their turn, the game ends, and the winner is the player that colored more nodes.
#
# You are the second player.  If it is possible to choose such a y to ensure you win the game,
# return true.  If it is not possible, return false.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# Output: true
# Explanation: The second player can choose the node with value 2.
#
#
# Constraints:
#
# root is the root of a binary tree with n nodes and distinct node values from 1 to n.
# n is odd.
# 1 <= x <= n <= 100


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _count_nodes(self, node):
        if not node:
            return 0

        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def _get_neighbours(self, node, x):
        if not node:
            return None

        if node.val != x:
            return self._get_neighbours(node.left, x) or self._get_neighbours(node.right, x)

        return [self._count_nodes(node.left), self._count_nodes(node.right)]

    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        node_counts = self._get_neighbours(root, x)

        if root.val != x:
            node_counts = [n - 1 - sum(node_counts)] + node_counts

        largest_count = sorted(node_counts)[-1]

        return largest_count > n - largest_count
