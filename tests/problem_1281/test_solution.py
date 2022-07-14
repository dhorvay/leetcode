import pytest
from leetcode.problem_1281 import Solution

params = [
    # n, output
    (234, 15),
    (4421, 21)
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.subtractProductAndSum(test_input) == expected
