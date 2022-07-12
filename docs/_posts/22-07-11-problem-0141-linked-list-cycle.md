---
title: Linked List Cycle
categories:
  - Solutions
tags:
  - Easy
  - Linked List
  - Hash Table
sidebar:
  nav: quick-links
---

Given ```head```, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the ```next``` pointer. Internally, ```pos``` is used to denote the index of the node that tail's ```next``` pointer is connected to. **Note that pos is not passed as a parameter.**

Return ```true``` *if there is a cycle in the linked list.* Otherwise, return ```false```.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:**
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Contraints:**
- The number of the nodes in the list is in the range [0, 10<sup>4</sup>].
- -10<sup>5</sup> <= Node.val <= 10<sup>5</sup>
- pos is -1 or a **valid index** in the linked-list.

**Follow up:** Can you solve it using ```O(1)``` (i.e. constant) memory?