from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = float('inf')
        max_sal = float('-inf')
        avg_sal = 0
        for sal in salary:
            avg_sal += sal
            min_sal = min(min_sal, sal)
            max_sal = max(max_sal, sal)
        return (avg_sal-(min_sal+max_sal))/(len(salary)-2)