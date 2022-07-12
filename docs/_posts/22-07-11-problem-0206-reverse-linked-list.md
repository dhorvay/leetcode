---
title:  Reverse Linked List
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

Given the ```head``` of a singly linked list, reverse the list, and return *the reversed list.*

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

**Constraints:**
- The number of nodes in the list is the range ```[0, 5000]```.
- ```-5000 <= Node.val <= 5000```

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

---

## Solution

### Reverse
Traverse through the list keeping track of the previous node and manipulate pointers to reverse the list. Define your typical ```curr``` pointer and assign it to the head of the given list. Another pointer, ```prev```, should also be defined, this will keep track of the last value traversed, initially set this to ```None``` as we want the first node's next pointer to point to ```None```. While traversing through the list keep the ```curr.next``` value in a temp variable, ```next```. Then set ```curr.next``` to ```prev```. Now we can set ```prev``` to the ```curr``` value, then finally ```curr``` can point to the temp variable we set up called ```next```. Return ```prev```. 

| Time | Space |
| ---- | ----- |
| O(n) | O(1)  |

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
```