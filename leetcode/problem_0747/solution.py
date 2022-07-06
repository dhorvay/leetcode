from typing import List

class Solution:
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