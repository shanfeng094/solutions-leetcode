"""
	021. Merge Two Sorted Lists
	@name: li jin
	@date: Mar 02, 2016
	@link: https://leetcode.com/problems/merge-two-sorted-lists/
	@time: 60 ms
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
