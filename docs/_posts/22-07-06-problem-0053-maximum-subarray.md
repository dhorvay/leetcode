---
title: Maximum Subarray
categories:
  - Solutions
tags:
  - Medium
  - Arrays
  - Dynamic Programming
sidebar:
  nav: quick-links
---
Given an integer array ```nums```, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A **subarray** is a **contiguous** part of an array.

**Example 1:**
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
**Example 2:**
```
Input: nums = [1]
Output: 1
```
**Example 3:**
```
Input: nums = [5,4,-1,7,8]
Output: 23
```
 

**Constraints:**

- ```1 <= nums.length <= 105```
- ```-104 <= nums[i] <= 104```

 

**Follow up:** If you have figured out the ```O(n)``` solution, try coding another solution using the **divide and conquer approach**, which is more subtle.



---
## Solution
---
### Brute Force
Calculate the sum of all subarrays and keep the largest.
Doesn't pass the LeetCode submission due to 'Time Limit Exceeded' for one of the test cases.


| Time | Space |
| ---- | ----- |
| O(n<sup>3</sup>)| O(1)|


```python
def maxSubArray_brute_On3(self, nums: List[int]) -> int:
    largest_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s = sum(nums[i:j+1])
            largest_sum = max(largest_sum, s)
    return largest_sum
```

### Brute Force, slightly improved
Calculate the sum of all subarrays and keep the largest, but slightly improved by keeping the current sum for each subarray calculation, so you don't need a third loop.
Doesn't pass the LeetCode submission due to 'Time Limit Exceeded' for one of the test cases.


| Time | Space |
| ---- | ----- |
| O(n<sup>2</sup>)| O(1)|


```python
def maxSubArray_brute_On2(self, nums: List[int]) -> int:
    largest_sum = float('-inf')
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            largest_sum = max(largest_sum, s)
    return largest_sum
```

###  Dynamic Programming
Create two variables, one for the ```largest_sum``` and another for the current sum, ```s```. Loop through the list, if at any point the current sum is negative, then it will not add to our largest sum, so you can "throw away" the previous values in the list. 

[Kadane's Algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm)


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|


```python
def maxSubArray(self, nums: List[int]) -> int:
    largest_sum = float('-inf')
    s = 0
    for num in nums:
        if s < 0:
            s = 0
        s += num
        largest_sum = max(largest_sum, s)
    return largest_sum
```

### TODO: Divide and Conquer