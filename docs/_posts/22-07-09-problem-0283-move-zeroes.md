---
title: Move Zeroes
categories:
  - Solutions
tags:
  - Easy
  - Arrays
  - Two Pointer
sidebar:
  nav: quick-links
---

Given an integer array ```nums```, move all ```0```'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

 

**Example 1:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
**Example 2:**
```
Input: nums = [0]
Output: [0]
```
 

**Constraints:**
- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 
**Follow up:** Could you minimize the total number of operations done?


---
## Solution
---
### Two Pointer
Initialize a left pointer, ```l```, this pointer will act as the partition between non-zero and zero elements. Use the right pointer ```r``` to check for non-zero elements. Each time we see a non-zero element we want to swap that element with ```l``` and increment, if it is a zero element then just increment the right pointer, ```r```. 


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def moveZeroes(self, nums: List[int]) -> None:
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l],nums[r] = nums[r], nums[l]
            l += 1
    return nums
```