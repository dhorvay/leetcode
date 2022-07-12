---
title: Running Sum of 1d Array
categories:
  - Solutions
tags:
  - Easy
  - Linked List
  - Prefix Sum
sidebar:
  nav: quick-links
---

Given an array ```nums```. We define a running sum of an array as ```runningSum[i] = sum(nums[0]…nums[i])```.

Return the running sum of ```nums```.


**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2:**
```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3:**
```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```
 
**Constraints:**
- ```1 <= nums.length <= 1000```
- ```-10^6 <= nums[i] <= 10^6```

---

## Solution

### Prefix Sum
Pretty straightforward, just set the current index to the sum of the current index plus the previous sums.


| Time | Space |
| ---- | ----- |
| O(n) | O(1)  |

```python
def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i-1]+nums[i]
    return nums
```