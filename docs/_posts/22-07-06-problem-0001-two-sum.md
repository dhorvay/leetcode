---
title: Two Sum
categories:
  - Solutions
tags:
  - Easy
  - Arrays
  - Hash Table
sidebar:
  nav: quick-links
---

Given an array of integers ```nums``` and an integer ```target```, return *indices of the two numbers such that they add up to ```target```*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.


**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```
 

**Constraints:**

-  2 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
- **Only one valid answer exists.**

 
**Follow-up:** Can you come up with an algorithm that is less than O(n<sup>2</sup>) time complexity?

---

## Solutions
---
### Brute Force
The brute force method is simple. It uses a nested loop to check all combinations of sums in the list against the target value.

| Time | Space |
| ---- | ----- |
| O(n<sup>2</sup>)| O(1)|

```python
def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i,j]
```
---
### Hash Table (Dictionary)

A better approach is to use a dictionary, ```prev_table```, to store the difference between the ```target``` value and the current ```num``` as we iterate through the list. In this way we are guaranteed that the difference, ```diff```, will appear in the list at some point after the current number if it the difference is already not the current index.
A downside of this approach is that it has a larger space complexity.

| Time | Space |
| ---- | ----- |
| O(n)| O(n)|

``` python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    prev_table = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in prev_table:
            return [prev_table[diff], idx]
        prev_table[num] = idx
```