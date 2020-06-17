# https://leetcode.com/problems/binary-tree-right-side-view/
# 199. Binary Tree Right Side View

# History:
# Facebook
# 1.
# Mar 15, 2020
# 2.
# Apr 22, 2020

# Given a binary tree, imagine yourself standing on the right side of it, return the values of
# the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionDFS(object):
    def _right_side_view(self, node, ret, curr_level):
        if not node:
            return

        if len(ret) <= curr_level:
            ret.append(node.val)
        else:
            ret[curr_level] = node.val

        self._right_side_view(node.left, ret, curr_level + 1)
        self._right_side_view(node.right, ret, curr_level + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        self._right_side_view(root, ret, 0)

        return ret


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionBFS(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        to_do = [root]
        ret = []

        while to_do:
            nxt_to_do = []
            ret.append(to_do[-1].val)

            for n in to_do:
                if n.left:
                    nxt_to_do.append(n.left)
                if n.right:
                    nxt_to_do.append(n.right)

            to_do = nxt_to_do

        return ret
