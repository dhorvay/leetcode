import pytest
from leetcode.problem_0066 import Solution

params = [
    # digits, output
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([9], [1,0])
]

@pytest.mark.parametrize("test_input,expected", params)
class TestSolution:
    def setup(self):
        self.solution = Solution()

    def test_solution(self, test_input, expected):
        assert self.solution.plusOne(test_input) == expected
