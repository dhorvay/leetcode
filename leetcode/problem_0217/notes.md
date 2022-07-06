## 217. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) ![easy](https://img.shields.io/static/v1?label=&message=Easy&color=green)
---
Given an integer array ```nums```, return ```true``` if any value appears at least twice in the array, and return ```false``` if every element is distinct.

 

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```
 

**Constraints:**
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

---
## Solution
---
### Hash Set
Initialize a set. For each element in the list, if the number appears in the set return ```True``` else add the element to the set. If all elements are exhausted, then there are no duplicates.


| Time | Space |
| ---- | ----- |
| O(n)| O(n)|

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    prev = set()
    for num in nums:
        if num in prev:
            return True
        prev.add(num)
    return False
```