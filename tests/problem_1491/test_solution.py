import pytest
from leetcode.problem_1491 import Solution

params = [
    # nums, output
    ([4000,3000,1000,2000], 2500.00000),
    ([1000,2000,3000], 2000.00000)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.average(test_input) == expected
