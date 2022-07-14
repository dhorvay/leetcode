---
title: Subtract the Product and Sum of Digits of an Integer
categories:
  - Solutions
tags:
  - Easy
  - Math
sidebar:
  nav: quick-links
---

Given an integer number ```n```, return the difference between the product of its digits and the sum of its digits.

**Example 1:**
```
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
```

**Example 2:**
```
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
```

**Constraints:**
- ```1 <= n <= 10^5```

---

## Solution

### Math
The trick here is to know how to break a number down into its digits. You can do this by using the modding the given integer by 10. This will get us the last digit of the given integer. For example, ```234%10 == 4```. Do the necessary processing of calculating the total sum and product. Then at the end of the loop be sure to prepare for the next digit by dividing the given integer by 10. For example ```234//10 == 23```, then ```23%10 == 3```.  

```python
def subtractProductAndSum(self, n: int) -> int:
    total_product = 1 
    total_sum = 0
    while n != 0:
        digit = n%10
        total_sum += digit
        total_product *= digit
        n //= 10
    return total_product - total_sum
```