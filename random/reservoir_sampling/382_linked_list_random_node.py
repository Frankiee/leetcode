# [Reservoir-Sampling]
# https://leetcode.com/problems/linked-list-random-node/
# 382. Linked List Random Node

# History:
# Facebook
# 1.
# Apr 14, 2020

# Given a singly linked list, return a random node's value from the linked list. Each node must
# have the same probability of being chosen.
#
# Follow up:
# What if the linked list is extremely large and its length is unknown to you? Could you solve
# this efficiently without using extra space?
#
# Example:
#
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom() should return either 1, 2, or 3 randomly. Each element should have equal
# probability of returning.
# solution.getRandom();


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        curr = self.head
        count = 0
        ret = None

        while curr:
            count += 1

            rdm = random.randint(1, count)
            if rdm == count:
                ret = curr

            curr = curr.next

        return ret.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
