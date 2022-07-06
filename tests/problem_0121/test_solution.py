import pytest
from leetcode.problem_0121 import Solution

params = [
    # prices, output
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.maxProfit(test_input) == expected
