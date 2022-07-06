## 283. [Move Zeroes](https://leetcode.com/problems/move-zeroes/) ![easy](https://img.shields.io/static/v1?label=&message=Easy&color=green)
---
Given an array, rotate the array to the right by ```k``` steps, where ```k``` is non-negative.

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```
 
**Constraints:**
- ```1 <= nums.length <= 105```
- ```-231 <= nums[i] <= 231 - 1```
- ```0 <= k <= 105```

**Follow up:**
- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with ```O(1)``` extra space?


---
## Solution
---
### Brute Force
Allocate another list to hold the values. As you move through the array move the element by ```k %= len(nums)```, this will ensure that the element gets moved to the right spot for rotation.


| Time | Space |
| ---- | ----- |
| O(n)| O(n)|

```python
def rotate_brute(self, nums: List[int], k: int) -> None:
    num_copy = nums.copy()
    for idx, num in enumerate(num_copy):
        nums[(idx+k)%len(nums)] = num
```

### Reverse
Reverse the list. Now you will notice the first partition defined by ```k```, we can reverse inplace and that will look like the result we want. The section after ```k``` until the end of the list can be reversed inplace too, so the entire array is rotated as needed.


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    self.reverse_inplace(nums, 0, n-1)
    self.reverse_inplace(nums, 0, k-1)
    self.reverse_inplace(nums, k, n-1)

def reverse_inplace(self, arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```