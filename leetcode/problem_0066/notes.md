## 66. [Plus One](https://leetcode.com/problems/plus-one/) ![easy](https://img.shields.io/static/v1?label=&message=Easy&color=green)
---
You are given a **large integer** represented as an integer array ```digits```, where each ```digits[i]``` is the i<sup>th</sup> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading ```0```'s.

Increment the large integer by one and return *the resulting array of digits.*

 

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```
 
**Constraints:**

- ```1 <= digits.length <= 100```
- ```0 <= digits[i] <= 9```
- ```digits``` does not contain any leading ```0```'s.



---
## Solution
---
### Carry Over
The trick here is that if the last digit is equal to 9, then to add one you must set that digit to 0 and 'carry over' a one to the next index. If all of the digits are equal to 9, then we must expand the list by 1.
Loop through the list in a reverse order. If the first digit is 9 then set the current digit to zero and increment, else add 1 to the current digit and return. If the first digit was 9, in the next iteration check again if the digit it 9, if not then increment by 1 and return, else continue until the digit is not 9. If all the digits were 9, then insert a 1 at the 0th index and return the list. 


| Time | Space |
| ---- | ----- |
| O(n)| O(n)*|

*In case of all 9s

```python
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    digits.insert(0,1)
    return digits
```