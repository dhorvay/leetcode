---
title:  Middle of the Linked List
categories:
  - Solutions
tags:
  - Easy
  - Linked List
  - Two Pointers
sidebar:
  nav: quick-links
---

Given the ```head``` of a singly linked list, return *the middle node of the linked list.*

If there are two middle nodes, return **the second middle** node.

**Example 1:**

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```

**Example 2:**
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

**Contraints:**
- The number of nodes in the list is in the range ```[1, 100]```.
- ```1 <= Node.val <= 100```

---
## Solutions

### Brute Force
Traverse the linked list one time to get the count of elements. Once the count is retrieved find the middle position. Then traverse the linked list one more to find the middle element.


| Time | Space |
| ---- | ----- |
| O(n)| O(n)|

```python
def middleNode_On(self, head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    middle = head
    while head is not None:
        count += 1
        head = head.next
    for i in range(0, count//2):
        middle = middle.next
    return middle
```

### Two Pointers
Define two pointers, one slow and one fast. If you move the fast point at a rate of twice the slow pointer, then by the time the fast pointer reaches the last element, the slow point will be at the middle element.


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```