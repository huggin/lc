# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        p = list1
        for _ in range(a - 1):
            p = p.next
        q = p.next
        p.next = list2
        while p.next is not None:
            p = p.next
        for _ in range(b - a + 1):
            q = q.next
        p.next = q
        return list1
