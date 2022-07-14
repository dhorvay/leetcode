class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total_product = 1 
        total_sum = 0
        while n != 0:
            digit = n%10
            total_sum += digit
            total_product *= digit
            n = n//10
        return total_product - total_sum