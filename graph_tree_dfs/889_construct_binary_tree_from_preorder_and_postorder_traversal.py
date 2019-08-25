# [Import, MultiTraversalSequence]
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# 889. Construct Binary Tree from Preorder and Postorder Traversal

# https://www.youtube.com/watch?v=53aOi0Drp9I&t=323s
# https://github.com/Frankiee/leetcode/blob/master/graph_tree_dfs_recursion/README.md

# Return any binary tree that matches the given preorder and postorder
# traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers,
# you can return any of them.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convert_from_pre_post(self, pre, post):
        if not pre:
            return None

        root_value_pre = pre.pop(0)
        root_value_post = post.pop()

        root = TreeNode(root_value_pre)

        for end in range(len(pre) + 1):
            # check left root
            if end > 0:
                left_root_pre = pre[0]
                left_root_post = post[end - 1]
                if left_root_pre != left_root_post:
                    continue
            # check right root
            if end < len(pre):
                right_root_pre = pre[end]
                right_root_post = post[-1]
                if right_root_pre != right_root_post:
                    continue

            left_pre = pre[:end]
            left_post = post[:end]
            right_pre = pre[end:]
            right_post = post[end:]

            left_root = self.convert_from_pre_post(left_pre, left_post)
            if left_root is False:
                continue
            right_root = self.convert_from_pre_post(right_pre, right_post)
            if right_root is False:
                continue
            root.left = left_root
            root.right = right_root

            return root

        return False

    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        return self.convert_from_pre_post(pre, post)
