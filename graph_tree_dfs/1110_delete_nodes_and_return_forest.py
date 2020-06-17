# https://leetcode.com/problems/delete-nodes-and-return-forest/
# 1110. Delete Nodes And Return Forest

# History:
# Google
# 1.
# Mar 9, 2020

# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union
# of trees).
#
# Return the roots of the trees in the remaining forest.  You may return the result in any order.
#
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#
#
# Constraints:
#
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _dfs(self, root, to_delete, ret, is_root):
        if not root:
            return
        if root.val in to_delete:
            self._dfs(root.left, to_delete, ret, True)
            self._dfs(root.right, to_delete, ret, True)

            return None

        if is_root:
            ret.append(root)

        root.left = self._dfs(root.left, to_delete, ret, False)
        root.right = self._dfs(root.right, to_delete, ret, False)

        return root

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ret = []
        to_delete = set(to_delete)

        self._dfs(root, to_delete, ret, True)

        return ret
