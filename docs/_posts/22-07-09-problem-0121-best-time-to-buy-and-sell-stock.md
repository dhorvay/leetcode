---
title: Best Time to Buy and Sell Stock
categories:
  - Solutions
tags:
  - Easy
  - Arrays
  - Dynamic Programming
  - Blind75
sidebar:
  nav: quick-links
---

You are given an array ```prices``` where ```prices[i]``` is the price of a given stock on the i<sup>th</sup> day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

*Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return ```0```*.

 

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```
**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```
 

**Constraints:**
- 1 <= prices.length <= 10<sup>5</sup>
- 0 <= prices[i] <= 10<sup>4</sup>



---
## Solution
---
### Dynamic Programming
We want to find the minimum price we can buy the stock for and also the highest price we can sell for that comes after the minimum price. To do this initialize the ```min_price``` as we loop through the list check if the current value is less that the ```min_price```, if it is, we have a new minimum, moreover as we loop through, we should also be calculating the ```max_profit```, which is the current value minus the current ```min_price``` so far. We want to continously compare max_profits in case we come across a new ```min_price``` where the ```max_price``` is less that the previous window.


| Time | Space |
| ---- | ----- |
| O(n)| O(1)|

```python
def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit            
```