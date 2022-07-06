from typing import List

class Solution:
    def productExceptSelf_On(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        postfix = [0]*n
        out = [0]*n
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        postfix[len(postfix)-1] = 1
        for j in range(n-2, -1, -1):
            postfix[j] = nums[j+1]*postfix[j+1]
        for k in range(len(out)):
            out[k] = prefix[k]*postfix[k]
        return out

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0]*n
        out[0] = 1
        for i in range(1, n):
            out[i] = nums[i - 1] * out[i - 1]
        postfix = 1
        for i in reversed(range(n)):
            out[i] = out[i] * postfix
            postfix *= nums[i]
        return out