import enum
from typing import List

class Solution:
    def rotate_brute(self, nums: List[int], k: int) -> None:
        num_copy = nums.copy()
        for idx, num in enumerate(num_copy):
            nums[(idx+k)%len(nums)] = num

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
