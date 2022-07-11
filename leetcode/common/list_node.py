from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def from_list(lst: List[int]) -> Optional[ListNode]: 
    if len(lst) == 0:
        return None
    if len(lst) == 1: 
        return ListNode(lst[0]) 
    else: 
        return ListNode(lst[0], from_list(lst[1:]))

def equals(ll1,ll2):
    while ll1 and ll2 and ll1.val == ll2.val:
        ll1 = ll1.next
        ll2 = ll2.next
    if not ll1 and not ll2:
        return True
    return False
