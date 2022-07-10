---
title: Count Odd Numbers in an Interval Range
categories:
  - Solutions
tags:
  - Easy
  - Arrays
  - Math
sidebar:
  nav: quick-links
---

Given two non-negative integers ```low``` and ```high```. Return the *count of odd numbers between ```low``` and ```high``` (inclusive).*

 

**Example 1:**
```
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
```

**Example 2:**
```
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
```
 

**Constraints:**

- ```0 <= low <= high <= 10^9```

---
## Solution

### Math
If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same, so it is the range divided by 2. Otherwise, if high and low are odd, then it is the range plus one.


| Time | Space |
| ---- | ----- |
| O(1)| O(1)|

```python
def countOdds(self, low: int, high: int) -> int:
    range = high-low+1
    if high%2 != 0 and low%2 !=0:
        return range//2+1
    return range//2
```