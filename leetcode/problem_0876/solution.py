from typing import Optional

from leetcode.common.list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode_On(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        middle = head
        while head is not None:
            count += 1
            head = head.next
        for i in range(0, count//2):
            middle = middle.next
        return middle

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow