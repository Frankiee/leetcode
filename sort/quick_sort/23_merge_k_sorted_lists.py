# [QuickSort]
# https://leetcode.com/problems/merge-k-sorted-lists/
# 23. Merge k Sorted Lists

# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def binary_insert(self, lst, lists):
        if not lists:
            lists.append(lst)
            return

        if lst.val < lists[0].val:
            lists.insert(0, lst)
            return
        if lst.val > lists[-1].val:
            lists.append(lst)
            return

        l, r = 0, len(lists) - 1

        while l <= r:
            mid = (l + r) / 2
            if lists[mid].val == lst.val:
                lists.insert(mid, lst)
                return
            elif lists[mid].val > lst.val:
                r = mid - 1
            else:
                l = mid + 1

        lists.insert(l, lst)

    def partition(self, lists, l, r):
        if r - l <= 0:
            return l

        pivot = lists[r].val

        for curr in range(l, r):
            if lists[curr].val < pivot:
                lists[curr], lists[l] = lists[l], lists[curr]
                l += 1
        lists[r], lists[l] = lists[l], lists[r]

        return l

    def quick_sort(self, lists, l, r):
        pivot = self.partition(lists, l, r)

        if pivot - 1 - l > 0:
            self.quick_sort(lists, l, pivot - 1)
        if r - (pivot + 1) > 0:
            self.quick_sort(lists, pivot + 1, r)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [lst for lst in lists if lst]

        if not lists:
            return None

        self.quick_sort(lists, 0, len(lists) - 1)

        res = ListNode(None)
        curr = res

        while lists:
            lst = lists.pop(0)
            curr.next = lst
            lst = lst.next
            curr = curr.next
            curr.next = None

            if lst:
                self.binary_insert(lst, lists)

        return res.next
