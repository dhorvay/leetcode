---
title: Product of Array Except Self
categories:
  - Solutions
tags:
  - Medium
  - Arrays
  - Prefix Sum
  - Blind75
sidebar:
  nav: quick-links
---

Given an integer array ```nums```, return an array ```answer``` such that ```answer[i]``` is equal to the product of all the elements of ```nums``` except ```nums[i]```.

The product of any prefix or suffix of ```nums``` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in ```O(n)``` time and without using the division operation.

 

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```
 
**Constraints:**

- 2 <= nums.length <= 10<sup>5</sup>
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of ```nums``` is **guaranteed** to fit in a **32-bit** integer.

 

**Follow up:** Can you solve the problem in ```O(1)``` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)


---
## Solution
---
### Prefix Sum O(n) Space
Initialize three arrays - one for the prefix product, one for the postfix product, and one for the ouput. 
Iterate through the input in a forward direction. As you iterate calculate the product of the current number, with the product of all numbers that came before it.
Do the same in the reverse direction to calulcate the postfix array.
Iterate through one more time and at each index take the product of the prefix and postfix at that index.


| Time | Space |
| ---- | ----- |
| O(n) | O(n)  |

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0]*n
    right = [0]*n
    res = [0]*n
    left[0] = 1
    for i in range(1, n):
        left[i] = nums[i-1]*left[i-1]
    right[len(right)-1] = 1
    for j in range(n-2, -1, -1):
        right[j] = nums[j+1]*right[j+1]
    for k in range(len(res)):
        res[k] = left[k]*right[k]
    return res
```

### Prefix Sum 'O(1)'
The idea is the same as the previous, but instead of having to initialize an array for prefix and postfix, do it all in the output array.


| Time | Space |
| ---- | ----- |
| O(n) | O(1)*  |
*According to the problem

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0]*n
    right = [0]*n
    res = [0]*n
    left[0] = 1
    for i in range(1, n):
        left[i] = nums[i-1]*left[i-1]
    right[len(right)-1] = 1
    for j in range(n-2, -1, -1):
        right[j] = nums[j+1]*right[j+1]
    for k in range(len(res)):
        res[k] = left[k]*right[k]
    return res
```