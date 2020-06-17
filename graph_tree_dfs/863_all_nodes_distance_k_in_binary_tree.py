# [Classic]
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# 863. All Nodes Distance K in Binary Tree

# History:
# Facebook
# 1.
# Mar 27, 2020
# 2.
# Apr 1, 2020
# 3.
# May 15, 2020

# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The
# answer can be returned in any order.
#
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
#
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# Accepted


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _get_distance_k_nodes(self, node, K):
        if not node:
            return []

        if K == 0:
            return [node.val]

        left_nodes = self._get_distance_k_nodes(node.left, K - 1)
        right_ndoes = self._get_distance_k_nodes(node.right, K - 1)

        left_nodes.extend(right_ndoes)

        return left_nodes

    def _distance_k(self, node, target, K):
        if not node:
            return None, None

        if node == target:
            return self._get_distance_k_nodes(node, K), 0

        left_nodes, left_distance = self._distance_k(node.left, target, K)
        if left_distance is not None:
            if left_distance == K - 1:
                left_nodes.append(node.val)
            elif K - left_distance - 2 >= 0:
                right_nodes = self._get_distance_k_nodes(node.right, K - left_distance - 2)
                left_nodes.extend(right_nodes)
            return left_nodes, left_distance + 1

        right_nodes, right_distance = self._distance_k(node.right, target, K)
        if right_distance is not None:
            if right_distance == K - 1:
                right_nodes.append(node.val)
            elif K - right_distance - 2 >= 0:
                left_nodes = self._get_distance_k_nodes(node.left, K - right_distance - 2)
                right_nodes.extend(left_nodes)
            return right_nodes, right_distance + 1

        return None, None

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        nodes, _ = self._distance_k(root, target, K)

        return nodes
