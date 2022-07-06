import pytest
from leetcode.problem_0747 import Solution

params = [
    # nums, output
    ([3,6,1,0], 1),
    ([1,2,3,4], -1),
    ([1], 0)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.dominantIndex(test_input) == expected
