# 67.69%, 99.12%
# 技巧点在于设置一个dumpy，传回的时候是从dumpy的第二个节点开始传。避免了边界问题（两个list都是0的情况）
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dumpy = ListNode()
        p = dumpy
        p1 = list1
        p2 = list2
        while (p1 is not None) and (p2 is not None):
            if p1.val < p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next
        while p1 is not None:
            p.next = p1.next
            p = p.next
            p1 = p1.next
        while p2 is not None:
            p.next = p2
            p = p.next
            p2 = p2.next

        return dumpy.next



