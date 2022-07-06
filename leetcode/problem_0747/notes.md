## 747. [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) ![easy](https://img.shields.io/static/v1?label=&message=Easy&color=green)
---
You are given an integer array ```nums``` where the largest integer is **unique.**

Determine whether the largest element in the array is **at least twice** as much as every other number in the array. If it is, return *the **index** of the largest element, or return ```-1``` otherwise.*

**Example 1:**
```
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
```
**Example 2:**
```
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
```
**Example 3:**
```
Input: nums = [1]
Output: 0
Explanation: 1 is trivially at least twice the value as any other number because there are no other numbers.
```
 
**Constraints:**

- ```1 <= nums.length <= 50```
- ```0 <= nums[i] <= 100```
- The largest element in ```nums``` is unique.

---
## Solution
---
### Straightforward
Iterate through ```nums``` twice for O(2n) complexity. The first loop is needed to capture the index of the ```largest_num```. The second loop is needed to test the condition that the ```largest_num``` is twice the value of all of the other elements in ```nums```. 

| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def dominantIndex(self, nums: List[int]) -> int:
    largest_num = float('-inf')
    largest_num_idx = -1
    for idx,num in enumerate(nums):
        if num > largest_num:
            largest_num = num
            largest_num_idx = idx
    for num in nums:
        if largest_num < num * 2 and largest_num != num:
            return -1
    return largest_num_idx
```