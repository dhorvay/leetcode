from typing import Optional

from leetcode.common.list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set = set()
        curr = head
        while curr:
            if curr.next in hash_set:
                return curr.next
            hash_set.add(curr)
            curr = curr.next
        return None