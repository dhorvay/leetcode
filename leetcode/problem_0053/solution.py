from typing import List

class Solution:
    def maxSubArray_brute_On3(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = sum(nums[i:j+1])
                largest_sum = max(largest_sum, s)
        return largest_sum

    def maxSubArray_brute_On2(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                largest_sum = max(largest_sum, s)
        return largest_sum

    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float('-inf')
        s = 0
        for num in nums:
            if s < 0:
                s = 0
            s += num
            largest_sum = max(largest_sum, s)
        return largest_sum