import pytest
from leetcode.problem_1991 import Solution

params = [
    # nums, output
    ([2,3,-1,8,4], 3),
    ([1,-1,4], 2),
    ([2,5], -1)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.findMiddleIndex(test_input) == expected
