import pytest
from leetcode.problem_0724 import Solution

params = [
    # nums, output
    ([1,7,3,6,5,6], 3),
    ([1,2,3], -1),
    ([2,1,-1], 0)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.pivotIndex(test_input) == expected
