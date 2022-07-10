---
title: Average Salary Excluding the Minimum and Maximum Salary
categories:
  - Solutions
tags:
  - Easy
  - Arrays
  - Sorting
sidebar:
  nav: quick-links
---

You are given an array of **unique** integers ```salary``` where ```salary[i]``` is the salary of the i<sup>th</sup> employee.

Return *the average salary of employees excluding the minimum and maximum salary.* Answers within 10<sup>-5</sup> of the actual answer will be accepted.

 

**Example 1:**
```
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
```

**Example 2:**
```
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
```
 
**Constraints:**

- 3 <= salary.length <= 100
- 1000 <= salary[i] <= 10<sup>6</sup>
- All the integers of salary are unique.

---

## Solution

### Sorting
In order to calculate the average salary, loop through the list while calculating the total sum, then divide by the total number of elements in the list. The trick here is you also need to keep track of the minimum and maximum salary as they are excluded from the total. When calculating the average, subtract the sum of the minimum and maximum salary, and when dividing ensure you subtract 2 from the total number of elements.


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def average(self, salary: List[int]) -> float:
    min_sal = float('inf')
    max_sal = float('-inf')
    avg_sal = 0
    for sal in salary:
        avg_sal += sal
        min_sal = min(min_sal, sal)
        max_sal = max(max_sal, sal)
    return (avg_sal-(min_sal+max_sal))/(len(salary)-2)
```