import pytest
from leetcode.problem_1523 import Solution

params = [
    # nums, output
    ((3,7), 3),
    ((8,10), 1)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.countOdds(*test_input) == expected
