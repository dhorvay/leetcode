class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range = high-low+1
        if high%2 != 0 and low%2 !=0:
            return range//2+1
        return range//2
