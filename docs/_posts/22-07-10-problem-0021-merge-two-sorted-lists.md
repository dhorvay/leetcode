---
title:  Merge Two Sorted Lists
categories:
  - Solutions
tags:
  - Easy
  - Linked List
  - Sorting
  - Blind75
sidebar:
  nav: quick-links
---

You are given the heads of two sorted linked lists ```list1``` and ```list2```.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

*Return the head of the merged linked list.*

**Example 1:**

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**
```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**
```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**
- The number of nodes in both lists is in the range ```[0, 50]```.
- ```-100 <= Node.val <= 100```
- Both ```list1``` and ```list2``` are sorted in **non-decreasing** order.

---

## Solution

### Sorting

Set up a placeholder node called ```prehead``` this allows us to return the head of the list at the end. Add a pointer to ```curr``` which will point to the current node as we traverse the lists.
Traverse both lists simultaneously with the condition that they have a ```.next``` pointer not equal to ```None```, and compare the value at each node. If the value in ```list1``` is greater than point ```curr``` to ```list2```, and vice versa. After traversing the trick now is to append the left over list to which ever list did not terminate the loop with the ```None``` condition.


| Time  | Space |
| ----  | ----- |
| O(n+m)| O(1)  |


```python
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    prehead = ListNode()
    curr = prehead
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next
    curr.next = list1 or list2
    return prehead.next
```
