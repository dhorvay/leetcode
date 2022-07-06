from typing import List

class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_table = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prev_table:
                return [prev_table[diff], idx]
            prev_table[num] = idx
